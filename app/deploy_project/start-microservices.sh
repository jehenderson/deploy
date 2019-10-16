#!/bin/bash
while ! nc -z mysql 3306; do echo sleeping; sleep 1; done; echo Connected!; sleep 10 && python manage.py makemigrations && python manage.py migrate && python manage.py flush --no-input -v 0 && python manage.py loaddata db.json && mod_wsgi-express start-server --working-directory /app --reload-on-changes /app/deploy_project/wsgi.py
