# Full-Stack Engineer (Product)

## About Sundew

Sundew builds submission intake software for commercial insurance underwriters. When a broker emails a carrier about a new risk, the attachments are a mess: scanned ACORD forms, five-year loss runs, a schedule of values in someone's private spreadsheet dialect. Underwriters spend hours retyping it before they can price anything.

Sundew reads that email and its attachments, extracts the risk into a structured submission, cross-checks it against prior years and against what the broker actually wrote, and hands the underwriter a clearance decision with every field traceable back to the page it came from. The models are the product, not a chat box bolted to the side.

We're 35 people, Series A, with paying carriers in the US and UK. Engineering is nine people and stays small on purpose.

## What you'll do

- Own features end to end: schema, extraction pipeline, API, and the underwriter-facing UI.
- Sit in on customer calls and underwriter shadowing sessions. Our best specs come from watching someone work.
- Build and maintain evals for the extraction and clearance steps. Every prompt change ships behind a scored eval run, not a vibe check.
- Work on the boring parts that make an LLM product trustworthy: document chunking, citation spans, confidence surfaces, human review queues, audit logs.
- Ship several times a week. We deploy from main, behind flags, with no release train.

## Requirements

- 5+ years building and running production web applications.
- Strong TypeScript. Our stack is Next.js (App Router), tRPC, Postgres with Drizzle, Inngest for background workflows, and Claude via the Anthropic API. Python for the eval harness.
- Real SQL skill. You can read a query plan and fix a bad index.
- Comfort with ambiguous, low-quality input data and with building UI for people whose job you don't have.
- You've shipped something with an LLM in the critical path and have opinions about where it broke.

## Nice to have

- Insurance, claims, or lending background.
- Document AI experience: OCR, layout models, PDF extraction.
- Design sense. There is no dedicated designer for internal-facing surfaces.

## Working arrangement

Remote within Europe, or hybrid from our Amsterdam office if you prefer one. Core hours overlap 10:00-16:00 CET; roughly a quarter of your customer calls will run late for US East Coast. We fly the whole company together for three days each quarter. No relocation support outside the EU, and we can sponsor a Dutch visa only for the hybrid track.
