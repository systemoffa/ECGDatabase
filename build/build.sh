#!/usr/bin/env bash

deactivate

rm -rf venv
virtualenv -p python2.7 venv
source venv/bin/activate
pip install --upgrade pip
pip install pybuilder
pyb install_dependencies
pyb publish
