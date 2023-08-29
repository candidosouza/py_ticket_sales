#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi
poetry config virtualenvs.in-project true
poetry install
mkdir -p /logs
chown -R 1000:1000 logs
tail -f /dev/null