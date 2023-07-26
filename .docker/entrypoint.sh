#!/bin/bash

if [ ! -f ".env" ]; then
  cp .env.example .env
fi
python -m pip install --upgrade pip
pip install -r requirements.txt
tail -f /dev/null