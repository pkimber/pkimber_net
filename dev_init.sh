py.test -x
touch temp.db && rm temp.db
django-admin.py migrate --noinput
django-admin.py init_app_block
django-admin.py init_app_compose
django-admin.py demo_data_login
django-admin.py demo_data_invoice
django-admin.py init_project
django-admin.py runserver
