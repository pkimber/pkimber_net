pkimber.net
***********

Development
===========

Install
-------

Virtual Environment
-------------------

::

  virtualenv --python=python3 venv-pkimber-net
  source venv-pkimber-net/bin/activate

  pip install -r requirements/local.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
-----

::

  ./init_dev.sh

Browse to http://localhost:8000/crm/contact/::

  user          staff
  password      letmein

If using test Postgres data downloaded from the live site::

  py.test -x && \
      django-admin.py migrate --noinput && \
      django-admin.py init_app_block && \
      django-admin.py runserver

Release and Deploy
==================

https://www.kbsoftware.co.uk/docs/
