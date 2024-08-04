FLAGS ?= --rm
CMD ?=

DOCKER_COMPOSE_FLAGS := docker compose

setup:
	@echo "Setting up environment files..."
	@cp frontend/.env.example frontend/.env
	@cp backend/.env.example backend/.env
	@echo "Done 🍺"

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