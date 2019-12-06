# -*- encoding: utf-8 -*-
from .local import *

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

# Celery
from kombu import Exchange, Queue

# transport
REDIS_HOST = get_env_variable("REDIS_HOST")
REDIS_PORT = get_env_variable("REDIS_PORT")
BROKER_URL = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)
CELERY_RESULT_BACKEND = "redis://{}:{}/0".format(REDIS_HOST, REDIS_PORT)
# number of worker processes (will be 3 == controller, worker and beat)
CELERYD_CONCURRENCY = 1
# rate limits
CELERY_DISABLE_RATE_LIMITS = True
# serializer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
# queue
CELERY_DEFAULT_QUEUE = DATABASE_NAME
CELERY_QUEUES = (
    Queue(DATABASE_NAME, Exchange(DATABASE_NAME), routing_key=DATABASE_NAME),
)

MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

INSTALLED_APPS += ("django_extensions", "debug_toolbar")

# force the debug toolbar to be displayed
def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
    "INTERCEPT_REDIRECTS": False,
    "ENABLE_STACKTRACES": True,
}
# INTERNAL_IPS = ('127.0.0.1',)
