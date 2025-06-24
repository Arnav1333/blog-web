#!/usr/bin/env bash

# Upgrade pip first
pip install --upgrade pip

# Install psycopg2-binary explicitly to avoid Python 3.13 incompatibility
pip install psycopg2-binary==2.9.9

# Install the rest of the requirements
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
