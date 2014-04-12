pkimber.net
***********

Development
===========

Install
-------

Virtual Environment
-------------------

Note: replace ``patrick`` with your name (checking in the ``settings`` folder
to make sure a file has been created for you)::

  mkvirtualenv p_pkimber_net
  pip install -r requirements/local.txt

  echo "export DJANGO_SETTINGS_MODULE=settings.dev_patrick" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset DJANGO_SETTINGS_MODULE" >> $VIRTUAL_ENV/bin/postdeactivate
  echo "export SECRET_KEY=\"the_secret_key\"" >> $VIRTUAL_ENV/bin/postactivate
  echo "unset SECRET_KEY" >> $VIRTUAL_ENV/bin/postdeactivate

  add2virtualenv .
  deactivate

Testing
-------

We use ``pytest-django``::

  workon p_pkimber_net
  find . -name '*.pyc' -delete
  py.test

To stop on first failure::

  py.test -x

Usage
-----

::

  workon p_pkimber_net

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
  password      staff

If using test Postgres data downloaded from the live site::

  workon p_pkimber_net

  py.test -x && \
      django-admin.py syncdb --noinput && \
      django-admin.py migrate --all --noinput && \
      django-admin.py init_app_cms && \
      django-admin.py runserver

Release and Deploy
==================

https://github.com/pkimber/docs
