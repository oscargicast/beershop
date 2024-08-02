FROM python:3.12.2-slim

ENV PYTHONUNBUFFERED=1 \
    # Prevents python creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    \
    # Pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    # Poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=1.7.1 \
    # Make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # Make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # Do not ask any interactive question
    POETRY_NO_INTERACTION=1 \
    \
    # Paths
    # this is where our requirements + virtual environment will live
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PYTHONPATH="/code/src"


  # Update image and install deps
RUN apt-get update \
    && apt-get -y install python3-dev libpq-dev build-essential gcc curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archives/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION
# Prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Run Poetry
WORKDIR $PYSETUP_PATH
COPY pyproject.toml ./
RUN poetry lock
RUN poetry install --only main --no-root

COPY src/ /code/src/
COPY tests/ /code/tests/

WORKDIR /code