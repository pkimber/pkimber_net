# -*- encoding: utf-8 -*-
from .local import *

from kombu import Exchange, Queue


DATABASE = "dev_www_pkimber_net_malcolm"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DATABASE,
        "USER": "malcolm",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

# MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES + (
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
# )

# Celery
# transport
BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
# number of worker processes (will be 3 == controller, worker and beat)
CELERYD_CONCURRENCY = 1
# rate limits
CELERY_DISABLE_RATE_LIMITS = True
# serializer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]
# queue
CELERY_DEFAULT_QUEUE = DATABASE
CELERY_QUEUES = (Queue(DATABASE, Exchange(DATABASE), routing_key=DATABASE),)


from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    "process_mail": {"task": "mail.tasks.process_mail", "schedule": crontab()}
}

# def show_toolbar(request):
#     return True
# SHOW_TOOLBAR_CALLBACK = show_toolbar

# INTERNAL_IPS = ['127.0.0.1']
