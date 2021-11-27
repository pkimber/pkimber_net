# -*- encoding: utf-8 -*-
from .local import *


DOMAIN = get_env_variable("DOMAIN")

DATABASE_NAME = get_env_variable("DATABASE_NAME")
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


REDIS_HOST = get_env_variable("REDIS_HOST")
REDIS_PORT = get_env_variable("REDIS_PORT")
# https://dramatiq.io/reference.html#middleware
DRAMATIQ_BROKER = {
    "BROKER": "dramatiq.brokers.redis.RedisBroker",
    "OPTIONS": {"url": "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)},
    "MIDDLEWARE": [
        # drops messages that have been in the queue for too long
        "dramatiq.middleware.AgeLimit",
        # cancels actors that run for too long
        "dramatiq.middleware.TimeLimit",
        # lets you chain success and failure callbacks
        "dramatiq.middleware.Callbacks",
        # automatically retries failed tasks with exponential backoff
        "dramatiq.middleware.Retries",
    ],
}
# KB Software queue name (to allow multiple sites on one server)
DRAMATIQ_QUEUE_NAME = DATABASE_NAME

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)
INSTALLED_APPS += ("django_extensions", "debug_toolbar")


DEBUG_TOOLBAR_CONFIG = {
    "ENABLE_STACKTRACES": True,
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": lambda r: DEBUG,
}
# INTERNAL_IPS = ('127.0.0.1',)
