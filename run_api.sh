#!/bin/bash

PYTHON="/usr/bin/python3"
DIR="venv"

$PYTHON -m venv $DIR
source $DIR/bin/activate

echo "************ Starting docker... ************"

docker-compose up -d

echo "************ Installing requirements... ************"

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python app/main.py
