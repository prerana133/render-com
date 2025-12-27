#!/bin/sh
set -e

cd /app

python manage.py migrate --noinput
python manage.py collectstatic --noinput


gunicorn baseproject.wsgi:application \
  --bind 0.0.0.0:"${PORT:-8000}" \
  --workers 2 \
  --timeout 120 \
  --log-file -