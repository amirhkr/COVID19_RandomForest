#!/bin/bash

echo "Ensure virtualenv is installed."
pip install virtualenv

echo "Create virtualenv in current directory called venv."
virtualenv venv

echo "Activate venv."
source venv/bin/activate

echo "Install requirements for project."
pip install -r requirements.txt

echo "Add venv kernel to jupyter."
python -m ipykernel install --user --name=venv --display-name="Python (covidlib)"

echo "Start jupyter lab."
jupyter lab
