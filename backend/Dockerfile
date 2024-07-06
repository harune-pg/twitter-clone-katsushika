FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip pip-tools

WORKDIR /code
COPY requirements.in requirements.in
RUN pip-compile requirements.in && pip-sync

COPY . .
