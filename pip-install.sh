#!/bin/bash

echo "Ensure virtualenv is installed."
pip install virtualenv

echo "Create virtualenv in current directory called venv."
virtualenv venv

echo "Activate venv."
source venv/bin/activate

echo "Install requirements for project."
pip install -r requirements.txt

echo "Install XGBOOST package"
conda install -c anaconda py-xgboost

echo "Add venv kernel to jupyter."
python -m ipykernel install --user --name=venv --display-name="Python (COVID19_RandomForest)"

echo "Start jupyter lab."
jupyter lab
