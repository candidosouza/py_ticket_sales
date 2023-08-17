#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi

poetry install
tail -f /dev/null