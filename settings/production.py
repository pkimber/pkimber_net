# -*- encoding: utf-8 -*-
from .base import *

DEBUG = False
TESTING = get_env_variable_bool("TESTING")

if get_env_variable_bool("SSL"):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [get_env_variable("ALLOWED_HOSTS")]

DOMAIN = get_env_variable("DOMAIN")
DATABASE_NAME = DOMAIN.replace(".", "_").replace("-", "_")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DATABASE_NAME,
        "USER": DATABASE_NAME,
        "PASSWORD": get_env_variable("DB_PASS"),
        "HOST": get_env_variable("DB_IP"),
        "PORT": "",
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
# KB Software queue name (to allow multiple sites on one server)
DRAMATIQ_QUEUE_NAME = DATABASE_NAME
DRAMATIQ_QUEUE_NAME_PIPELINE = DATABASE_NAME

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# https://django-sendfile2.readthedocs.io/en/latest/backends.html#nginx-backend
SENDFILE_BACKEND = "django_sendfile.backends.nginx"
SENDFILE_ROOT = get_env_variable("SENDFILE_ROOT")
SENDFILE_URL = "/private"

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)
