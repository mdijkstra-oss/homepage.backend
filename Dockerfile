# Chancery serving this repository's config/, as one image: a Go builder that
# fetches the published module, then a scratch stage holding the static binary,
# the CA bundle and the configuration.

# 1.26.5 is the floor chancery's go.mod declares. The tag is a full patch
# release rather than the floating 1.26-alpine, so the compiler that produces
# the deployed binary is decided here and not by what the tag pointed at on the
# day CI ran.
FROM golang:1.26.5-alpine AS build

# The final stage has no package manager, and an HTTPS backend without a
# certificate bundle fails at the handshake in a way that reads as an outage.
RUN apk add --no-cache ca-certificates

# proxy.golang.org caches a published version's contents permanently and
# sum.golang.org records its checksum, so this string resolves to the same bytes
# forever: a tag moved in git afterwards surfaces as a checksum mismatch rather
# than as different software under the same name.
ARG CHANCERY_VERSION=v0.1.0

# CGO off is what makes the binary static, which is what a scratch final stage
# can hold. -s -w drop the symbol table and DWARF; -trimpath keeps build paths
# out of the binary.
RUN CGO_ENABLED=0 GOOS=linux go install -trimpath -ldflags="-s -w" \
    "github.com/mdijkstra-oss/chancery/cmd/chancery@${CHANCERY_VERSION}"

FROM scratch

COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=build /go/bin/chancery /chancery

# A Serverless Container mounts no volumes, so the configuration is baked and
# the image is the unit of version.
COPY config /config

# Numeric, because scratch carries no /etc/passwd for a name to resolve against.
USER 65532:65532

# Set here rather than left to chancery's own default, because infra declares
# 8081 on the container and aims its liveness probe at it. A chancery version
# whose default moved would otherwise bind elsewhere and fail that probe with
# nothing in either repository naming the port it actually chose.
ENV PORT=8081

EXPOSE 8081

# chancery's --config defaults to ./config, which resolves against this.
WORKDIR /

ENTRYPOINT ["/chancery"]
CMD ["serve"]

# The binary checks itself: a scratch image holds no shell, no curl and no wget,
# so any other command named here would be one the image cannot execute.
HEALTHCHECK --interval=5s --timeout=3s --start-period=2s --retries=5 \
    CMD ["/chancery", "healthcheck", "--addr", "127.0.0.1:8081"]
