# Local loops, in order of what they cost.
IMAGE ?= homepage-backend:dev

# Where homepage.site is checked out, and where `ask` sends. Both are overridable:
# AGENT_URL=https://agent.mdijkstra.dev/cv make ask Q="..." talks to production.
#
# The harness is the same compose service under a second project name, so `make up`
# on 8081 and the harness on 8090 can run side by side.
SITE_REPO ?= ../site
HARNESS_PORT ?= 8090
HARNESS ?= homepage-backend-harness
HARNESS_COMPOSE = BACKEND_PORT=$(HARNESS_PORT) docker compose -p $(HARNESS)
AGENT_URL ?= http://localhost:$(HARNESS_PORT)/cv
export SITE_REPO
export AGENT_URL

.PHONY: build validate list up seed ask serve stop restart

build:
	docker build --tag $(IMAGE) .

# Against the built image, so the validator is the same build as the server.
validate: build
	docker run --rm $(IMAGE) validate

list: build
	docker run --rm $(IMAGE) list

up:
	docker compose up

# End-to-end conversation harness. `seed` pulls the background material the
# frontend pushes; `ask` replays it, plus any prior turns, against the agent.
scripts/node_modules:
	cd scripts && npm install

seed: scripts/node_modules
	@cd scripts && npx tsx seed.ts > seed.json
	@echo "scripts/seed.json"

# Starts the agent if it is not already up, and does nothing if it is. --wait blocks
# on the image's healthcheck, so `ask` never fires at a socket that is not listening.
# The config is mounted, so a prompt edit needs `make restart`, not a rebuild.
serve:
	@test -f .env || { echo "No .env — copy .env.example and fill it in."; exit 1; }
	@# One shell: `exit` in a make recipe ends its own line, not the recipe.
	@if [ -n "$$($(HARNESS_COMPOSE) ps -q backend 2>/dev/null)" ]; then exit 0; fi; \
	if lsof -nP -iTCP:$(HARNESS_PORT) -sTCP:LISTEN >/dev/null 2>&1; then \
		echo "Port $(HARNESS_PORT) is taken by something else. Set HARNESS_PORT."; exit 1; \
	fi; \
	printf 'starting %s on %s' "$(HARNESS)" "$(HARNESS_PORT)"; \
	if $(HARNESS_COMPOSE) up -d --wait >/dev/null 2>&1; then echo " · ready"; else \
		echo " · never came up"; $(HARNESS_COMPOSE) logs --tail 20; exit 1; \
	fi

stop:
	@$(HARNESS_COMPOSE) down >/dev/null 2>&1 || true

# Prompt edits land on a restart: the container reads config/ when it boots.
restart: stop serve

# make ask Q="What did he build at PeerWell?" [TURNS=conversations/example.json] [SAVE=1]
ask: scripts/node_modules scripts/seed.json serve
	@cd scripts && npx tsx ask.ts "$(Q)" $(if $(TURNS),--turns $(TURNS),) $(if $(SAVE),--save,)

scripts/seed.json:
	@$(MAKE) seed
