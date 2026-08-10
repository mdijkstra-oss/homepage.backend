# Local loops, in order of what they cost. CHANCERY points at whatever serves
# this repository's config/: the built image by default, or a binary built from
# a chancery checkout while the module is not yet published.
IMAGE ?= homepage-backend:dev
# host-gateway is how the container reaches the stub on the host. Docker Desktop
# resolves host.docker.internal on its own; a Linux runner does not, and the
# symptom there is a 503 rather than a name error.
CHANCERY ?= docker run --rm -i --add-host=host.docker.internal:host-gateway \
	-e RESPONSES_BASE_URL={base_url} -p {port}:8081 $(IMAGE) serve
AGENT_URL ?= http://127.0.0.1:8081/cv

.PHONY: build validate list test test-live up

build:
	docker build --tag $(IMAGE) .

# Against the built image, so the validator is the same build as the server.
validate: build
	docker run --rm $(IMAGE) validate

list: build
	docker run --rm $(IMAGE) list

# No provider, no key, no network beyond loopback.
test:
	python3 tests/contract_test.py --chancery "$(CHANCERY)"

# Costs money and is not deterministic. Run it when the prompt changes.
# HISTORY takes the input items the site pushes, so grounding is exercised.
test-live:
	python3 tests/live_test.py --url $(AGENT_URL) $(if $(HISTORY),--history $(HISTORY),)

up:
	docker compose up
