# homepage.backend

The chat backend for `mdijkstra.dev`. One Markdown prompt in `config/`, served over HTTP by [chancery](https://github.com/mdijkstra-oss/chancery), shipped as a single container image that runs on a Scaleway Serverless Container.

Requests and replies are [`openai-responses`](https://platform.openai.com/docs/api-reference/responses). Chancery writes the agent's model, instructions and sampling fields onto the body it received, `POST`s the result to `{RESPONSES_BASE_URL}/responses`, and relays the event stream back untouched. DeepSeek serves that format natively, so nothing translates between them.

The configuration is baked into the image, so the image is the unit of version: the bytes CI validated are the bytes that serve, deploying is a tag and rolling back is the previous tag.

## Routes

| route | method | answers |
|---|---|---|
| `/health` | `GET` | `200` with the body `ok` |
| `/cv` | `POST` | the backend's event stream, relayed per event |
| `/cv/responses` | `POST` | the same, for a caller whose SDK appends `/responses` to its base URL |

Every other path is `404`.

```sh
curl -N -X POST localhost:8081/cv \
  -H 'Content-Type: application/json' \
  -d '{"input":[{"type":"message","role":"user","content":"Where is Matthijn based?"}],"stream":true}'
```

`stream` decides the response shape: `true` gets `200 text/event-stream` with each event flushed as it arrives, omitted or `false` gets one JSON response object. The events a client reads are `response.output_text.delta`, carrying `delta`, and `response.failed`, carrying the message at `response.error.message`.

A failure that arrives as an event arrives inside a `200`, because the status is already sent by then. Statuses chancery produces itself:

| status | when |
|---|---|
| `400` | the body is not a JSON object, or it exceeds 10 MB |
| `404` | no route matches, with or without the `/responses` suffix |
| `429` | DeepSeek answered `429` to all three attempts; the caller gets a bare `429` carrying the text `Too Many Requests`, and DeepSeek's own body goes to the log |
| `503` | DeepSeek was unreachable, or sent no response headers within 45 seconds |
| `502` | any other failure to obtain an answer |

Any other status DeepSeek returns is relayed verbatim, body included.

Two timeouts bound a request that has started, neither of them configurable: chancery gives up if response headers do not arrive within 45 seconds, and ends a started stream that goes 90 seconds without data. A stream ended that second way stops mid-sequence with no terminal event and no error status, so treat a stream that ends without `response.completed` as a failure rather than a short answer.

## Configuration

`config/` is the whole of what this repository configures.

| file | holds |
|---|---|
| `config/models.yaml` | one alias, `fast`, naming the model |
| `config/cv/index.md` | the agent |

The route is the directory name, so `config/cv/index.md` is what defines `POST /cv`. Renaming the directory renames the route, and [the site](https://github.com/mdijkstra-oss/homepage.site) and [infra](https://github.com/mdijkstra-oss/homepage.infra) take the path from here.

The `fast` alias names the bare model id `deepseek-v4-flash`, with no prefix: the value travels in the request body verbatim and DeepSeek is reached directly. `chancery validate` checks that an alias resolves, not what it resolves to, so a prefixed id passes validation and fails at request time as a backend error.

The agent's frontmatter:

| field | value |
|---|---|
| `description` | the one-line description `chancery list` prints beside the route |
| `model` | `fast` |
| `reasoning_effort` | `low` |
| `max_tokens` | `1200` |

`reasoning_effort: low` turns a default down. DeepSeek V4 Flash has thinking mode enabled by default at effort `high`, so leaving the field unset means every visitor question is deliberated over at that latency and that token cost. `low` is the least reasoning the flat `reasoning_effort` field documents.

`max_tokens: 1200` sits above the longest legitimate answer and bounds what a single request can cost. Chancery writes it over the caller's `max_output_tokens`, so it is a ceiling a caller cannot raise.

## Local development

Three loops, in order of what they cost. All three run against the built image, so build it first:

```sh
docker build -t homepage-backend .
```

### Validating and listing

No server, no key, no network. This is the same invocation CI makes, so a configuration that passes here passes there.

```sh
docker run --rm homepage-backend validate
docker run --rm homepage-backend list
```

```text
PATH  MODEL              REASONING
cv    deepseek-v4-flash  low
1 agents · 1 models
```

### One turn against the real model

Needs the key and still no server. Copy `.env.example` to `.env`, fill in the [variables](#environment), and send a single turn:

```sh
docker run --rm --env-file .env homepage-backend call cv --input "Where is Matthijn based?"
```

The stream renders as text, and the command exits non-zero when the backend reports a failure — enough to see whether a prompt edit changed an answer.

### The whole HTTP surface

```sh
docker compose up
```

One service, built from this directory, publishing `8081` and reading `.env`. It mounts `./config` read-only over the baked copy, which makes a prompt edit cost a restart rather than a rebuild. That mount is the only shape that differs from production, where the baked copy is what serves.

## Tests

Two suites, split by what they cost.

`make test` runs the contract cases against a scripted stub standing in for DeepSeek, so it needs no key, no network beyond loopback and no deployment. It covers the body chancery composes — the bare model id, the agent's `max_output_tokens` written over the caller's, `reasoning.effort`, the prompt in front of the caller's own instructions, and the absence of `store` — plus the route table, the status contract, the rate-limit path and CORS. The stub is the only place the composed body can be inspected, which is most of why it exists.

```sh
make test          # ~15 seconds
make test-slow     # adds the stalled-stream case, which waits out chancery's 90-second bound
```

CI runs `make test-slow` against the image it just built, and the release workflow runs it again before the push.

`make test-live` needs the key and costs money, so it runs when the prompt changes rather than on every push. It checks that both exits the agent offers resolve — the address is `hire@mdijkstra.dev` and the CV link is the site-relative `/resume.pdf` — and puts five hostile visitor turns to the real model. Those five are graded by a reader: the mechanical check catches a hostile claim adopted as fact, but the property under test is whether every statement about Matthijn is traceable to the background material, and only a person can settle that.

```sh
make test-live AGENT_URL=http://127.0.0.1:8081/cv HISTORY=history.json
```

`HISTORY` is the input-item array the site pushes. Without it the exits are still exercised, but grounding is not, because there is no background material for the model to stay inside.

## Exposure

The deployed container is public, unauthenticated, and spends money per request.

> [!WARNING]
> Anyone who learns the URL can spend the DeepSeek key, and no mechanism stops them. `CORS_ORIGINS` is not a control against this: it stops a browser on another origin, and `curl` ignores it entirely. Scaleway offers no rate limiting in front of a Serverless Container, and chancery has none either.

Authentication is off deliberately. Chancery's JWT middleware needs an issuer and a key source, and a public homepage has no logged-in visitors to issue tokens to, so `AUTH_JWT_*` stays unset and every request that reaches the container is served.

What exists are bounds on how much that costs:

- `max_tokens: 1200` caps output per request, and cannot be raised from outside.
- A small `max_scale` on the container, paired with a per-instance concurrency of one, caps requests in flight. It takes both: instances alone bound nothing if each accepts many requests at once. Infra sets the two numbers.
- A bounded prepaid balance on the DeepSeek account, with automatic top-up off, caps the total. This is the only bound that is hard.

Two paths spend more than they look like they should. Input tokens are not capped by `max_tokens`, and chancery's 10 MB body limit is a compile-time constant, so one request may carry as much input as DeepSeek's context window accepts. And a request with no `input` at all is still a valid request, because chancery always supplies `instructions` and DeepSeek requires only one of the two — an empty body gets an answer and a bill.

The residual risk is bounded rather than removed: draining the prepaid balance stops the chat until it is topped up, and the loss is capped at that balance.

The key belongs to a DeepSeek account used by nothing else, and is never committed. `.env` holds it locally and is in `.gitignore`; in production it is a Scaleway secret environment variable on the container. The image never contains it, and neither does the registry.

## Releasing

One tag names everything that ships.

1. Edit `VERSION` to the new semver, without the leading `v`, and commit it.
2. Tag that commit `vX.Y.Z` and push the tag.

The release workflow fails if the tag disagrees with `VERSION`, builds the image, runs `validate` against the image it just built, and pushes to `rg.nl-ams.scw.cloud/mdijkstra-homepage/homepage-backend:<tag>`. The tag is the git tag verbatim, including the leading `v`.

The push is write-once: the workflow fails if the tag already exists in the registry rather than overwriting it, so a tag always means one image. Scaleway Container Registry has no tag-immutability setting, so this workflow is the only thing enforcing that. A fix gets a new tag.

Nothing is live until infra pins the tag as `backend_release` and applies. Rolling back names an earlier tag, and any tag ever pushed stays available.

Pushing needs two repository secrets, `REGISTRY_PUSH_ACCESS_KEY` and `REGISTRY_PUSH_SECRET_KEY`, holding the `registry-push` IAM key that infra produces.

Both halves of what produces the binary are pinned in the `Dockerfile`: the builder's `FROM` names a full Go patch release, and the `CHANCERY_VERSION` build argument's default names the chancery version. Bumping either is editing that one line.

## Environment

Every variable chancery reads that this deployment sets. Infra sets all of them on the container; `.env` sets them locally.

| variable | holds |
|---|---|
| `RESPONSES_BASE_URL` | `https://api.deepseek.com`. Chancery appends `/responses`. It has no default and `serve` refuses to boot without it. |
| `RESPONSES_AUTH_TOKEN` | the DeepSeek API key, raw. Chancery sends it as `Authorization: Bearer <value>`. |
| `PORT` | `8081`, which is the image's default. |
| `CORS_ORIGINS` | comma-separated origins a browser may call from. Empty denies every cross-origin request. |
| `ENV` | `production` on the container, `development` locally. |
| `LOG_LEVEL` | `info`. |

`CORS_ORIGINS` is whichever origin the site is served from, which infra owns and which changes when a custom domain lands. Getting it wrong is visible immediately: the browser blocks the request and the container logs a request it served anyway.

`SHUTDOWN_TIMEOUT` and `LOG_REQUEST_HEADERS` keep their defaults. The site sends neither `X-Session-ID` nor `X-Project-ID`, so the logging default matches nothing.

Logs are JSON on stdout and hold the route, the model, a request ID and the error text of a failure. They never hold the request body.

## See also

- [chancery](https://github.com/mdijkstra-oss/chancery) — the server, its CLI, and the full frontmatter set.
- [homepage.site](https://github.com/mdijkstra-oss/homepage.site) — the browser client that calls `/cv`, and the source of the contact address and CV link the prompt offers.
- [homepage.infra](https://github.com/mdijkstra-oss/homepage.infra) — the registry, the container, and every credential.
- [DeepSeek's Responses API guide](https://api-docs.deepseek.com/guides/responses_api/) — which parameters that endpoint supports.
