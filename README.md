# site-prompts

The prompt bundle for **mdijkstra.dev**, packaged as a self-contained,
versioned container image.

This repo holds the system prompts and provider config that power the site's
assistant — currently the `cv` portfolio chat — and nothing else. It is not an
application: it carries no Go code and no engine. It is *configuration* for
[Dragoman](https://codeberg.org/mdijkstra/dragoman), which turns each
Markdown prompt into a live HTTP endpoint. This repo bakes that config onto the
published Dragoman image and publishes the result, on tag, to a private
registry.

## Three repos, one seam

The work is split across three repos, joined at the container registry:

| Repo | Owns |
|---|---|
| **reed** (Dragoman) | The engine — the binary that serves prompts. Publishes the base image `codeberg.org/mdijkstra/dragoman`. |
| **site-prompts** (here) | The config — the prompts and their provider aliases. Bakes them onto the base and publishes a runnable image. |
| **infra** | The registry the image lands in (Scaleway `mdijkstra-homepage`) and the credential that pushes to it. |

Dragoman is the reusable engine; this repo is one deployment of it. You do not
rebuild the engine to ship a config change any more than you rebuild `node` to
ship a Node app — the base image is a dependency, pinned by digest.

## Layout

```
config/
  cv/                # the portfolio-chat prompt (Markdown, one file = one endpoint)
  providers.yaml     # provider + model aliases, trimmed to what the prompts use
Dockerfile           # FROM the Dragoman base, COPY config/ in
.woodpecker.yml      # tag-triggered build + push to the private registry
docs/plans/          # the requirements/implementation plan for this repo
```

## Why bake the config in

Dragoman is built to keep config *outside* the image and mount it at `/config`
at runtime. This repo deliberately does the opposite: it copies `config/` into
a derived image.

The reason is the artifact. Baking gives one immutable, content-addressed thing
to pull, pin, and roll back — a release you can point a server at by digest and
know exactly what it's running. Mounting loose files gives none of that: the
config can drift from the binary and there is no single versioned object.

The trade-off is honest: because the config is baked, **any prompt or provider
change ships as a new tagged image**. That is the point, not a bug — immutability
over live-editability.

## Trimmed providers

`config/providers.yaml` declares only the providers the bundled prompts actually
reference. Today that is **gemini alone**, because the `cv` prompt runs on
`gemini-3.5-flash` and nothing else — so the running image needs only a
`GEMINI_API_KEY`. Add a prompt that targets another model, add its provider
here, and ship a new tag.

Secrets are never committed or baked. API keys are supplied to the container at
runtime, not build time.

## Releasing

Publishing is tag-driven. Ordinary commits and pull requests build nothing.

```sh
git tag v1.2.3
git push origin v1.2.3
```

A tag push runs the Woodpecker pipeline, which pulls the digest-pinned Dragoman
base from Codeberg, copies `config/` in, and pushes the image to the private
Scaleway registry `mdijkstra-homepage` under a full tag set:

```
1.2.3   1.2   1   sha-<short-commit>   latest
```

The semver ladder lets a consumer pin as loosely or tightly as it wants; the
`sha-` tag ties every image back to an exact commit.

The build crosses two registries — it **pulls** the public base from Codeberg
and **pushes** the private image to Scaleway. The push credential is a dedicated
registry-push identity defined in the infra repo (mirroring its object-storage
`artifacts-upload` identity) and stored as a Woodpecker secret; it is never in
this repo.

## Running an image

The published image *is* Dragoman with the prompts baked in — it inherits the
base's entrypoint, so it serves with no extra config mount:

```sh
docker run --rm -p 8081:8081 \
  -e GEMINI_API_KEY=... \
  rg.nl-ams.scw.cloud/mdijkstra-homepage/site-prompts:latest
```

Deploying it (where it runs, how secrets and auth are wired) lives outside this
repo.
