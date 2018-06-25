# Flask REST application skeleton

REST application using Flask.

## Versions

App | Version
--- | ---
Python | 3.6.5
Flask | 1.0.2

# Setup & Run

## Copy git repository

    # Clone repository
    git clone https://github.com/KenanBek/flask-rest-skeleton.git
    # Move to project's folder
    cd django-rest-skeleton

## Configure and run on local machine
    python -m venv env
    source ./env/bin/activate
    pip install -r requirements.txt
    cd src
    export FLASK_APP=webapp.py
    python -m flask run

## Check code styling

After you have activated env you can check code styling using PyLint or PEP8 (pycodestyle).

    pylint src/.
    pycodestyle src/.
