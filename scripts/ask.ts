// Sends one question through the agent with the site's background material and any
// prior turns in front of it, exactly as the browser would, and prints the answer.
//
// Usage: npx tsx ask.ts ") question" [--turns conversations/x.json] [--save]

import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const AGENT_URL = process.env.AGENT_URL ?? 'http://localhost:8081/cv';

type Role = 'user' | 'assistant';
interface Turn {
  role: Role;
  content: string;
}
interface ChatMessage extends Turn {
  type: 'message';
}

const args = process.argv.slice(2);
const save = args.includes('--save');
const turnsPath = readOption(args, '--turns');
const question = args.filter((arg) => !arg.startsWith('--') && arg !== turnsPath).join(' ').trim();

if (!question) {
  console.error('Usage: npx tsx ask.ts "question" [--turns conversations/x.json] [--save]');
  process.exit(1);
}

const seed = readJson<ChatMessage[]>(resolve(HERE, 'seed.json'), 'Run `make seed` first.');
const turns = turnsPath ? readJson<Turn[]>(resolve(HERE, turnsPath)) : [];

const input: ChatMessage[] = [
  ...seed,
  ...turns.map((turn): ChatMessage => ({ type: 'message', role: turn.role, content: turn.content })),
  { type: 'message', role: 'user', content: question },
];

console.error(`${AGENT_URL} · ${seed.length} seed + ${turns.length} turns + 1 question`);

const answer = await streamAnswer(input);
process.stdout.write('\n');

if (save && turnsPath) {
  const grown: Turn[] = [...turns, { role: 'user', content: question }, { role: 'assistant', content: answer }];
  writeFileSync(resolve(HERE, turnsPath), `${JSON.stringify(grown, null, 2)}\n`);
  console.error(`\nAppended both turns to ${turnsPath}`);
}

async function streamAnswer(messages: ChatMessage[]): Promise<string> {
  const res = await fetch(AGENT_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'text/event-stream' },
    body: JSON.stringify({ input: messages, stream: true }),
  });
  if (!res.ok || !res.body) {
    console.error(`\nRequest failed (${res.status}): ${await res.text()}`);
    process.exit(1);
  }

  let answer = '';
  let completed = false;
  for await (const record of readEventStream(res.body)) {
    if (record.event === 'response.completed') completed = true;
    if (record.event === 'response.failed') {
      console.error(`\nInference failed: ${record.data}`);
      process.exit(1);
    }
    if (record.event !== 'response.output_text.delta') continue;
    const delta = (JSON.parse(record.data) as { delta?: string }).delta ?? '';
    answer += delta;
    process.stdout.write(delta);
  }

  if (!completed) {
    console.error('\nThe answer was cut off before it finished.');
    process.exit(1);
  }
  return answer;
}

// The same server-sent-event shape the frontend reads: `event:` and `data:` lines,
// a record per blank line.
async function* readEventStream(body: ReadableStream<Uint8Array>) {
  const decoder = new TextDecoder();
  let buffer = '';
  let event = '';
  let data: string[] = [];

  for await (const chunk of body) {
    buffer += decoder.decode(chunk, { stream: true });
    const lines = buffer.split('\n');
    buffer = lines.pop() ?? '';
    for (const raw of lines) {
      const line = raw.endsWith('\r') ? raw.slice(0, -1) : raw;
      if (line === '') {
        if (event) yield { event, data: data.join('\n') };
        event = '';
        data = [];
      } else if (line.startsWith('event:')) {
        event = line.slice(6).trim();
      } else if (line.startsWith('data:')) {
        data.push(line.slice(5).trim());
      }
    }
  }
  if (event) yield { event, data: data.join('\n') };
}

function readOption(argv: string[], name: string): string | undefined {
  const at = argv.indexOf(name);
  return at === -1 ? undefined : argv[at + 1];
}

function readJson<T>(path: string, hint = ''): T {
  try {
    return JSON.parse(readFileSync(path, 'utf8')) as T;
  } catch {
    console.error(`Cannot read ${path}. ${hint}`.trim());
    process.exit(1);
  }
}
