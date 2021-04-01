#!/usr/bin/env bash

VENVNAME=startrek_venv

python -m venv $VENVNAME
source $VENVNAME/scripts/activate
pip install --upgrade pip --user

test -f requirements.txt && pip install -r requirements.txt
python -m spacy download en_core_web_sm
deactivate
echo "build $VENVNAME"
