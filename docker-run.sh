#!/bin/bash

cd /var/www/auratus/auratus/
python manage.py migrate --noinput --settings=auratus.settings_docker
python manage.py collectstatic --noinput --settings=auratus.settings_docker
python manage.py compress --settings=auratus.settings_docker
exec gunicorn --env \
  DJANGO_SETTINGS_MODULE=auratus.settings_docker \
  auratus.wsgi:application -b 0.0.0.0:8000 -w 3 \
  --access-logfile=- --error-logfile=-
