# syntax=docker/dockerfile:1

# Bakes this repo's Dragoman config onto the published engine image. This repo
# adds no code — the base already carries the binary, entrypoint, and serve
# default; we only layer config/ on top.
#
# Pinned by digest so builds are reproducible and content-addressed. This is the
# current published base (the ci-test build); repin to a released digest once
# reed publishes semver tags.
FROM codeberg.org/mdijkstra/dragoman@sha256:e451121f3bc29a3770b6e6ca5b362b436f6fd3e3b247c37a03e3526843e1449f

COPY config/ /config/
