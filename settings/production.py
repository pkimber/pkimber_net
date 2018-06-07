# -*- encoding: utf-8 -*-
from .base import *

DEBUG = False
TESTING = get_env_variable_bool('TESTING')

if get_env_variable_bool('SSL'):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [get_env_variable('ALLOWED_HOSTS'), ]

DOMAIN = get_env_variable('DOMAIN')
DATABASE = DOMAIN.replace('.', '_')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE,
        'USER': DATABASE,
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': get_env_variable('DB_IP'),
        'PORT': '',
    }
}

# Celery
from kombu import Exchange, Queue
# transport
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# number of worker processes (will be 3 == controller, worker and beat)
CELERYD_CONCURRENCY = 1
# rate limits
CELERY_DISABLE_RATE_LIMITS = True
# serializer
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
# queue
CELERY_DEFAULT_QUEUE = DATABASE
CELERY_QUEUES = (
    Queue(DATABASE, Exchange(DATABASE), routing_key=DATABASE),
)

from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'update_search_index': {
        'task': 'search.tasks.update_search_index',
        'schedule': crontab(minute='15', hour='*/1'),
    },
}

ELASTIC_APM = {
    'DISABLE_SEND': get_env_variable_bool('MONITOR_DISABLE_SEND'),
    'SERVER_URL': get_env_variable('MONITOR_SERVER_URL'),
    'SERVICE_NAME': DATABASE,
}

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = get_env_variable("SENDFILE_ROOT")
SENDFILE_URL = '/private'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)
