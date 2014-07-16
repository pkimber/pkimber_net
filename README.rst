pkimber.net
***********

Development
===========

Install
-------

Virtual Environment
-------------------

::

  pyvenv-3.4 --without-pip venv-pkimber_net
  source venv-pkimber_net/bin/activate
  wget https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  python get-pip.py

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py init_app_block && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_crm && \
      django-admin.py demo_data_invoice && \
      django-admin.py init_project && \
      django-admin.py runserver

Browse to http://localhost:8000/crm/contact/::

  user          staff
  password      letmein

If using test Postgres data downloaded from the live site::

  py.test -x && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py init_app_block && \
      django-admin.py runserver

Release and Deploy
==================

https://django-dev-and-deploy-using-salt.readthedocs.org/
