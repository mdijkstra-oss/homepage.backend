# Chancery serving this repository's config/, as one image: a Go builder that
# fetches the published module, then an alpine stage holding the static binary,
# the log shipper and the configuration.

# 1.26.5 is the floor chancery's go.mod declares. The tag is a full patch
# release rather than the floating 1.26-alpine, so the compiler that produces
# the deployed binary is decided here and not by what the tag pointed at on the
# day CI ran.
FROM golang:1.26.5-alpine AS build

# proxy.golang.org caches a published version's contents permanently and
# sum.golang.org records its checksum, so this string resolves to the same bytes
# forever: a tag moved in git afterwards surfaces as a checksum mismatch rather
# than as different software under the same name.
ARG CHANCERY_VERSION=v0.2.0

# CGO off is what makes the binary static, so it links against no libc at all.
# -s -w drop the symbol table and DWARF; -trimpath keeps build paths out of the
# binary.
RUN CGO_ENABLED=0 GOOS=linux go install -trimpath -ldflags="-s -w" \
    "github.com/mdijkstra-oss/chancery/cmd/chancery@${CHANCERY_VERSION}"

# Alpine rather than scratch: a Serverless Container has no host to run a log
# collector on and no second container to put one beside, so the shipper is
# carried here, and it needs a shell and curl that scratch cannot hold.
FROM alpine:3.22

RUN apk add --no-cache curl jq

COPY --from=build /go/bin/chancery /chancery

COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
COPY docker/ship.sh /usr/local/bin/ship.sh

ENV BETTERSTACK_SERVICE=backend

# A Serverless Container mounts no volumes, so the configuration is baked and
# the image is the unit of version.
COPY config /config

USER 65532:65532

# Set here rather than left to chancery's own default, because infra declares
# 8081 on the container and aims its liveness probe at it. A chancery version
# whose default moved would otherwise bind elsewhere and fail that probe with
# nothing in either repository naming the port it actually chose.
ENV PORT=8081

EXPOSE 8081

# chancery's --config defaults to ./config, which resolves against this.
WORKDIR /

ENTRYPOINT ["/usr/local/bin/entrypoint.sh", "/chancery"]
CMD ["serve"]

HEALTHCHECK --interval=5s --timeout=3s --start-period=2s --retries=5 \
    CMD ["/chancery", "healthcheck", "--addr", "127.0.0.1:8081"]
