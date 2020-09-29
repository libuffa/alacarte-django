#!/bin/sh

set -e

python manage.py collecstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module app.wsgi