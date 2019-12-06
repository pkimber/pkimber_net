# -*- encoding: utf-8 -*-
from .local import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test_www_pkimber_net",
        "USER": get_env_variable("DATABASE_USER"),
        "PASSWORD": get_env_variable("DATABASE_PASS"),
        "HOST": get_env_variable("DATABASE_HOST"),
        "PORT": get_env_variable("DATABASE_PORT"),
    }
}

# http://docs.celeryproject.org/en/2.5/django/unit-testing.html
CELERY_ALWAYS_EAGER = True

# this is supposed to speed up tests
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
