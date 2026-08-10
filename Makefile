# Local loops, in order of what they cost.
IMAGE ?= homepage-backend:dev

.PHONY: build validate list up

build:
	docker build --tag $(IMAGE) .

# Against the built image, so the validator is the same build as the server.
validate: build
	docker run --rm $(IMAGE) validate

list: build
	docker run --rm $(IMAGE) list

up:
	docker compose up
