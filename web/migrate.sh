#!/bin/bash
SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USER}

cd /app/
/opt/venv/bin/python manage.py migrate --noinput

/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --username $SUPERUSER_USERNAME --noinput || true