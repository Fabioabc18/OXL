#!/bin/bash

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements and collect static files
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput