// Prints the background material the frontend pushes into every conversation, in the
// wire format it posts. Imported from the site repo rather than copied, so it cannot
// drift from what visitors actually get.
//
// Usage: npx tsx seed.ts > seed.json    (SITE_REPO overrides the checkout it reads)

import { existsSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
// Relative paths are read from the repo root, not from scripts/, so `../site` means
// what it looks like it means. resolve() ignores the base when given an absolute path.
const SITE_REPO = resolve(HERE, '..', process.env.SITE_REPO ?? '../site');
const HISTORY_MODULE = resolve(SITE_REPO, 'src/features/portfolio/chat/portfolioChatHistory.ts');

interface ChatMessage {
  type: 'message';
  role: 'user' | 'assistant';
  content: string;
}

if (!existsSync(HISTORY_MODULE)) {
  console.error(`No site checkout at ${SITE_REPO}\nSet SITE_REPO to where homepage.site lives.`);
  process.exit(1);
}

const { PORTFOLIO_CHAT_HISTORY } = (await import(pathToFileURL(HISTORY_MODULE).href)) as {
  PORTFOLIO_CHAT_HISTORY: readonly ChatMessage[];
};

process.stdout.write(`${JSON.stringify(PORTFOLIO_CHAT_HISTORY, null, 2)}\n`);
