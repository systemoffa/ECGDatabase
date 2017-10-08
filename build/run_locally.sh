#!/usr/bin/env bash

deactivate

rm -rf venv_deploy
virtualenv -p python2.7 venv_deploy
source venv_deploy/bin/activate
pip install --upgrade pip
pip install target/dist/ECGDatabase-1.0/dist/ECGDatabase-*.tar.gz

ecg_database runserver
