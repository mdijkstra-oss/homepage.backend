# syntax=docker/dockerfile:1

# Bakes this repo's Dragoman config onto the published engine image. This repo
# adds no code — the base already carries the binary, entrypoint, and serve
# default; we only layer config/ on top.
#
# Pin the base by digest before release (Prerequisite 4): replace the tag below
# with codeberg.org/mdijkstra/dragoman@sha256:<digest> so builds are reproducible
# and content-addressed. The tag form here is a placeholder for local iteration.
FROM codeberg.org/mdijkstra/dragoman:latest

COPY config/ /config/
