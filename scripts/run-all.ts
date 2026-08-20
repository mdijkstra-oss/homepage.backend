// Replays every scenario in scenarios.md against the agent and writes the answers to
// one markdown file, so two models can be compared on the same questions.
//
// Usage: npx tsx run-all.ts runs/out.md [--note "which model"] [--only K] [--concurrency 4]

import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const AGENT_URL = process.env.AGENT_URL ?? 'http://localhost:8081/cv';
const FIT_PREFIX = 'Is he a good fit?';

type Role = 'user' | 'assistant';
interface Turn {
  role: Role;
  content: string;
}
interface ChatMessage extends Turn {
  type: 'message';
}
interface Case {
  id: string;
  title: string;
  ask: string;
  question: string;
  turns: Turn[];
}

const args = process.argv.slice(2);
const only = readOption(args, '--only');
const note = readOption(args, '--note');
const concurrency = Number(readOption(args, '--concurrency') ?? 4);
const outPath = args.find(
  (arg) => !arg.startsWith('--') && arg !== only && arg !== note && arg !== String(concurrency),
);

if (!outPath) {
  console.error('Usage: npx tsx run-all.ts runs/out.md [--only K] [--concurrency 4]');
  process.exit(1);
}

const seed = readJson<ChatMessage[]>(resolve(HERE, 'seed.json'), 'Run `make seed` first.');
const cases = parseCases(readFileSync(resolve(HERE, 'scenarios.md'), 'utf8'))
  .filter((one) => (only ? one.id.startsWith(only) : true));

if (cases.length === 0) {
  console.error(only ? `No cases start with ${only}.` : 'No cases found in scenarios.md.');
  process.exit(1);
}

console.error(`${AGENT_URL} · ${cases.length} cases · ${concurrency} at a time`);

const answers = await mapWithLimit(cases, concurrency, async (one) => {
  const answer = await ask(one);
  console.error(`${one.id} ${answer.startsWith('FAILED') ? 'failed' : 'done'}`);
  return answer;
});

writeFileSync(resolve(HERE, outPath), render(cases, answers));
console.error(`\n${outPath}`);

// `**A1. One line**` opens a case, `Ask:` opens its ask block, `Want:` closes it. The
// last quoted string in that block is the question; a fixture is pasted under it, and
// a conversation file supplies the turns that come before it.
function parseCases(scenarios: string): Case[] {
  const found: Case[] = [];
  let open: { id: string; title: string; ask: string[] } | null = null;
  let reading = false;

  for (const line of scenarios.split('\n')) {
    const header = line.match(/^\*\*([A-Z]\d+)\. (.+)\*\*$/);
    if (header) {
      if (open) push(open);
      open = { id: header[1], title: header[2], ask: [] };
      reading = false;
      continue;
    }
    if (!open) continue;
    if (line.startsWith('Ask:')) {
      reading = true;
      open.ask.push(line.slice(4).trim());
    } else if (line.startsWith('Want:') || line.startsWith('Result:')) {
      reading = false;
    } else if (reading && line.trim()) {
      open.ask.push(line.trim());
    }
  }
  if (open) push(open);
  return found;

  function push(one: { id: string; title: string; ask: string[] }) {
    const ask = one.ask.join(' ');
    const quotes = [...ask.matchAll(/"([^"]*)"/g)].map((match) => match[1]);
    const fixture = ask.match(/`(fixtures\/[^`]+)`/)?.[1];
    const turnsPath = ask.match(/`(conversations\/[^`]+)`/)?.[1];
    const last = quotes.at(-1);

    if (!fixture && !last) return; // "Ask: anything." and anything else with no question
    const question = fixture
      ? `${last ?? FIT_PREFIX}\n\n${readFileSync(resolve(HERE, fixture), 'utf8').trim()}`
      : (last as string);

    found.push({
      id: one.id,
      title: one.title,
      ask,
      question,
      turns: turnsPath ? readJson<Turn[]>(resolve(HERE, turnsPath)) : [],
    });
  }
}

function render(all: Case[], answers: string[]): string {
  const body = all.map((one, at) => {
    const before = one.turns
      .map((turn) => `> **${turn.role}:** ${turn.content.split('\n').join('\n> ')}`)
      .join('\n>\n');
    return [
      `### ${one.id} ${one.title}`,
      '',
      `**Ask:** ${one.ask}`,
      ...(before ? ['', '**Turns before it:**', '', before] : []),
      '',
      answers[at],
    ].join('\n');
  });
  const intro = `${all.length} cases from scenarios.md, answers quoted as they came back.`;
  return `${['# Answers', '', note ? `${note}\n\n${intro}` : intro, '', ...body].join('\n')}\n`;
}

async function ask(one: Case): Promise<string> {
  const input: ChatMessage[] = [
    ...seed,
    ...one.turns.map((turn): ChatMessage => ({ type: 'message', ...turn })),
    { type: 'message', role: 'user', content: one.question },
  ];
  try {
    return await streamAnswer(input);
  } catch (error) {
    return `FAILED: ${error instanceof Error ? error.message : String(error)}`;
  }
}

async function streamAnswer(messages: ChatMessage[]): Promise<string> {
  const res = await fetch(AGENT_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Accept: 'text/event-stream' },
    body: JSON.stringify({ input: messages, stream: true }),
  });
  if (!res.ok || !res.body) throw new Error(`request failed (${res.status}): ${await res.text()}`);

  let answer = '';
  let completed = false;
  for await (const record of readEventStream(res.body)) {
    if (record.event === 'response.completed') completed = true;
    if (record.event === 'response.failed') throw new Error(`inference failed: ${record.data}`);
    if (record.event !== 'response.output_text.delta') continue;
    answer += (JSON.parse(record.data) as { delta?: string }).delta ?? '';
  }
  if (!completed) throw new Error('the answer was cut off before it finished');
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

async function mapWithLimit<In, Out>(items: In[], limit: number, run: (item: In) => Promise<Out>): Promise<Out[]> {
  const out = new Array<Out>(items.length);
  let next = 0;
  const workers = Array.from({ length: Math.min(limit, items.length) }, async () => {
    while (next < items.length) {
      const at = next++;
      out[at] = await run(items[at]);
    }
  });
  await Promise.all(workers);
  return out;
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
