#!/usr/bin/env bash

VENVNAME=network

python -m venv $VENVNAME
source $VENVNAME/scripts/activate
pip install --upgrade pip

test -f requirements.txt && pip install -r requirements.txt

echo "build $VENVNAME"