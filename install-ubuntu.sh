#!/usr/bin/env bash

#install script: virtual environment for ITU KSAMLDS1KU
#$ source install.sh

echo "Setting up virtual environment for python 3:"
virtualenv -p python3.10 venv
source ./venv/bin/activate

pip install --upgrade pip

echo "Installing all required python3 packages:"
pip install -r requirements.txt

pip list
echo "Installing python3 packages done."

echo "Please copy all raw data files to data/"

echo "All done."
