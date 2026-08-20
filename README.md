# homepage.backend

The chat endpoint behind [mdijkstra.dev](https://mdijkstra.dev).

It is a configuration directory for [chancery](https://github.com/mdijkstra-oss/chancery), which serves Markdown files as HTTP endpoints. Chancery's README covers the format; this one covers what is in here.

## The agent

`config/cv/index.md` answers `POST /cv` on `gpt-oss-120b`. Its frontmatter picks the model, its body is the prompt.

[homepage.site](https://github.com/mdijkstra-oss/homepage.site) pushes his background material into the conversation as input items, the prompt here is prepended with extra instructions.

## Running it

```sh
cp .env.example .env     # RESPONSES_BASE_URL and RESPONSES_AUTH_TOKEN
make up
```

`compose.yaml` mounts `./config` read-only over the copy the image baked, so a prompt edit locally costs a restart rather than a rebuild. Production mounts nothing.

## Testing a conversation

`scripts/` replays a whole conversation against the agent from the terminal, without a
browser. It reads the background material straight out of the site repo, so what it sends
is what a visitor sends.

```sh
make seed                                    # pull the background material -> scripts/seed.json
make ask Q="What did he build at PeerWell?"  # seed + question -> answer
```

`ask` starts the agent itself if it is not already up, and reuses it on every run after
that. `make stop` takes it down and `make restart` picks up a prompt edit.

It is the same compose service as `make up`, under a second project name and on port 8090
instead of 8081, so the two run side by side and `make stop` never touches the other one.
`HARNESS_PORT` moves it, and `AGENT_URL` points the question somewhere else entirely,
production included.

`seed` imports `PORTFOLIO_CHAT_HISTORY` from a homepage.site checkout, `../site` by
default and `SITE_REPO` otherwise.

Prior turns live in `scripts/conversations/*.json` as a plain list of roles and content.
Pass one to ask a follow-up in context, and add `SAVE=1` to append the exchange so the
next run picks up where this one stopped.

```sh
make ask Q="Which of those was hardest?" TURNS=conversations/example.json SAVE=1
```

## Releasing

The tag is the release, and `VERSION` has to match it. CI builds the image, validates the configuration inside it and pushes it. `CHANCERY_VERSION` in the `Dockerfile` pins the chancery release that goes in.

## License

Released under the [Zero-Clause BSD](LICENSE) (0BSD) license — public-domain-equivalent, do whatever you like, no attribution required.

## See also

- [chancery](https://github.com/mdijkstra-oss/chancery) — the server this configures.
- [homepage.site](https://github.com/mdijkstra-oss/homepage.site) — the frontend it answers.
- [homepage.infra](https://github.com/mdijkstra-oss/homepage.infra) — the Scaleway container and the tag it pins.
