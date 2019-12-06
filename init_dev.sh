#!/bin/bash
# exit immediately if a command exits with a nonzero exit status.
set -e
# treat unset variables as an error when substituting.
set -u

PGPASSWORD=$DATABASE_PASS psql --host $DATABASE_HOST --port $DATABASE_PORT -U $DATABASE_USER -c "DROP DATABASE IF EXISTS $DATABASE_NAME;"
PGPASSWORD=$DATABASE_PASS psql --host $DATABASE_HOST --port $DATABASE_PORT -U $DATABASE_USER -c "CREATE DATABASE $DATABASE_NAME TEMPLATE=template0 ENCODING='utf-8';"

django-admin.py migrate --noinput
django-admin.py init_app_block
django-admin.py init_app_compose
django-admin.py init_app_enquiry
django-admin.py demo_data_login
django-admin.py init_project
django-admin.py runserver 0.0.0.0:8000
