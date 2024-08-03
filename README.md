# Beershop

The challengue is described in the [CHALLENGUE.md](CHALLENGUE.md) file.

## Description

The domain model was implemented in the [`backend/domain`](backend/domain) and the UML model is the following:

![model](assets/model.svg)

## Requirements

- Docker and docker compose.
- Poetry (**optional**, for local virtualenv). Python 3.12 required.

## Building the containers

```sh
make build
```

### Creating a local virtualenv with poetry (optional)

```sh
poetry install --no-root
```

### Running the tests

```sh
make test
# Or, if you have a local virtualenv.
poetry run pytest
```

### Formatting and linting

```sh
make mypy
make black
```

### Makefile

There are more useful commands in the [Makefile](Makefile), have a look and try them out.

## Running the API server

This runs the API server in the local machine in the port 8000.
```sh
make runserver
```

When the local server is running [the orders are populated using this script](backend/populate.py).

**Here you can see the populated orders in your local machine:**
- http://localhost:8000/api/v1/orders/order-1/
- http://localhost:8000/api/v1/orders/order-2/