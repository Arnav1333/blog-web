#!/usr/bin/env bash

pip install --upgrade pip



# ✅ Install requirements (psycopg 3 will be used)
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput
