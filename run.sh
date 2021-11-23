#!/bin/sh
export FLASK_APP=index.py
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
flask run -h 0.0.0.0