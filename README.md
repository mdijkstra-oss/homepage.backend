# homepage.backend

The chat agent behind [mdijkstra.dev](https://mdijkstra.dev): a prompt, a model, and the build that ships them.

It is a configuration directory for [chancery](https://github.com/mdijkstra-oss/chancery), which serves Markdown files as HTTP endpoints. Chancery's README covers the format; this one covers what is in here.

## The agent

`config/cv/index.md` answers `POST /cv` on `deepseek-v4-flash`. Its frontmatter picks the model, its body is the prompt.

It knows nothing about Matthijn on its own. [homepage.site](https://github.com/mdijkstra-oss/homepage.site) pushes his background material into the conversation as input items, and the prompt makes that the only admissible source of fact. Anything a visitor supplies is data, never instruction.

## Running it

```sh
cp .env.example .env     # RESPONSES_BASE_URL and RESPONSES_AUTH_TOKEN
make up
```

`compose.yaml` mounts `./config` read-only over the copy the image baked, so a prompt edit locally costs a restart rather than a rebuild. Production mounts nothing.

## Tests

`make test` runs the image against a scripted stub backend, so it needs no provider and no key. It is not a second chancery suite: it covers what this configuration puts in the outbound body and the routes it produces, so a `CHANCERY_VERSION` bump has a gate before the site sees it.

`make test-live` needs the real model, so it costs money and a reader grades the answers. It exercises the prompt end to end, hostile visitor turns included. Run it when the prompt changes.

## Releasing

The tag is the release, and `VERSION` has to match it. CI builds the image, validates the configuration inside it, runs the tests and pushes it.

## License

Released under the [Zero-Clause BSD](LICENSE) (0BSD) license — public-domain-equivalent, do whatever you like, no attribution required.

## See also

- [chancery](https://github.com/mdijkstra-oss/chancery) — the server this configures.
- [homepage.site](https://github.com/mdijkstra-oss/homepage.site) — the frontend it answers.
- [homepage.infra](https://github.com/mdijkstra-oss/homepage.infra) — the Scaleway container and the tag it pins.
