# homepage.backend

The chat endpoint behind [mdijkstra.dev](https://mdijkstra.dev).

It is a configuration directory for [chancery](https://github.com/mdijkstra-oss/chancery), which serves Markdown files as HTTP endpoints. Chancery's README covers the format; this one covers what is in here.

## The agent

`config/cv/index.md` answers `POST /cv` on `deepseek-v4-flash`. Its frontmatter picks the model, its body is the prompt.

[homepage.site](https://github.com/mdijkstra-oss/homepage.site) pushes his background material into the conversation as input items, the prompt here is prepended with extra instructions.

## Running it

```sh
cp .env.example .env     # RESPONSES_BASE_URL and RESPONSES_AUTH_TOKEN
make up
```

`compose.yaml` mounts `./config` read-only over the copy the image baked, so a prompt edit locally costs a restart rather than a rebuild. Production mounts nothing.

## Releasing

The tag is the release, and `VERSION` has to match it. CI builds the image, validates the configuration inside it and pushes it. `CHANCERY_VERSION` in the `Dockerfile` pins the chancery release that goes in.

## License

Released under the [Zero-Clause BSD](LICENSE) (0BSD) license — public-domain-equivalent, do whatever you like, no attribution required.

## See also

- [chancery](https://github.com/mdijkstra-oss/chancery) — the server this configures.
- [homepage.site](https://github.com/mdijkstra-oss/homepage.site) — the frontend it answers.
- [homepage.infra](https://github.com/mdijkstra-oss/homepage.infra) — the Scaleway container and the tag it pins.
