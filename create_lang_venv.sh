#!/usr/bin/env bash

VENVNAME=lang101

python -m venv $VENVNAME
source $VENVNAME/scripts/activate
pip install --upgrade pip --user

pip install ipython
pip install jupyter

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt

deactivate
echo "build $VENVNAME"
