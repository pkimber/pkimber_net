# -*- encoding: utf-8 -*-
from .local import *


DATABASE_NAME = "dev_test_www_kbsoftware_co_uk"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DATABASE_NAME,
        "USER": get_env_variable("DATABASE_USER"),
        "PASSWORD": get_env_variable("DATABASE_PASS"),
        "HOST": get_env_variable("DATABASE_HOST"),
        "PORT": get_env_variable("DATABASE_PORT"),
    }
}

DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.stub.StubBroker",
    "OPTIONS": {},
    "MIDDLEWARE": [
        "dramatiq.middleware.AgeLimit",
        "dramatiq.middleware.TimeLimit",
        "dramatiq.middleware.Callbacks",
        "dramatiq.middleware.Pipelines",
        "dramatiq.middleware.Retries",
    ],
}
# KB Software queue name (to allow multiple sites on one server)
DRAMATIQ_QUEUE_NAME = DATABASE_NAME
DRAMATIQ_QUEUE_NAME_PIPELINE = DATABASE_NAME

# this is supposed to speed up tests
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
