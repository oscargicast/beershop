# Beershop

The challengue is described in the [CHALLENGUE.md](CHALLENGUE.md) file.

## Description

The domain model was implemented in the [`src/domain`](src/domain) and the UML model is the following:

![model](assets/model.svg)

## Requirements

- Docker and docker compose.
- Poetry (optional, for local virtualenv). Python 3.12 required.

## Building the containers


```sh
make build
```

### Creating a local virtualenv with poetry (optional)

```sh
poetry install --no-root
```

## Running the tests

```sh
make test
# Or, if you have a local virtualenv.
poetry run pytest
```

## Formatting and linting

```sh
make mypy
make black
```

## Makefile

There are more useful commands in the [Makefile](Makefile), have a look and try them out.

