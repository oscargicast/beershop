# These will speed up builds, for docker compose >= 1.25
export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

FLAGS ?= --rm

# Common flags for Docker Compose commands
DOCKER_COMPOSE_FLAGS := docker compose

all: down build up test

build:
	$(DOCKER_COMPOSE_FLAGS) build

up:
	$(DOCKER_COMPOSE_FLAGS) up $(filter-out $@,$(MAKECMDGOALS))

down:
	$(DOCKER_COMPOSE_FLAGS) down --remove-orphans

test:
	$(DOCKER_COMPOSE_FLAGS) run --rm app pytest -s $(filter-out $@,$(MAKECMDGOALS))

logs:
	$(DOCKER_COMPOSE_FLAGS) --tail=25 app

black:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} app black -l 86 $$(find * -name '*.py')

mypy:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} app mypy src tests

runserver:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} -it --service-ports app fastapi dev src/main.py --app=app --host=0.0.0.0 --port=8000

bash:
	$(DOCKER_COMPOSE_FLAGS) run ${FLAGS} -it app $(filter-out $@,$(MAKECMDGOALS)) /bin/sh

%:
	@: