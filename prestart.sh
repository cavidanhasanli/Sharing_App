#!/bin/bash

python manage.py migrate && python manage.py collectstatic --no-input
celery -A Sharing_Settings worker -B -l info &