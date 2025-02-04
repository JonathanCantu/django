#!/bin/bash

source venv/bin/activate

python --version
python -m django --version

# Start from scratch assuming we already have postgres server and psql already installed:
dropdb -U postgres "periodic_table"
createdb -U postgres "periodic_table"
psql -d "postgres://postgres:postgres@localhost/periodic_table" -f periodic_table.sql
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
