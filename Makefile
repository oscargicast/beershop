FLAGS ?= --rm
CMD ?=

DOCKER_COMPOSE_FLAGS := docker compose

build:
	$(DOCKER_COMPOSE_FLAGS) build $(filter-out $@,$(MAKECMDGOALS))

up:
	$(DOCKER_COMPOSE_FLAGS) up $(filter-out $@,$(MAKECMDGOALS))

down:
	$(DOCKER_COMPOSE_FLAGS) down --remove-orphans $(filter-out $@,$(MAKECMDGOALS))

logs:
	$(DOCKER_COMPOSE_FLAGS) logs --follow $(filter-out $@,$(MAKECMDGOALS))

%:
	@: