#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi
poetry config virtualenvs.in-project true
poetry install
tail -f /dev/null