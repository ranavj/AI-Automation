FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /code

# psycopg2 (Postgres) ke liye system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Pure project copy (simple & robust)
COPY . /code

# pyproject.toml se install
RUN python -m pip install --upgrade pip setuptools wheel \
 && pip install -e .
