FROM python:3.12.0-bookworm

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PATH="/virtual-bartender/.venv/bin:$PATH"

WORKDIR /virtual-bartender

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]