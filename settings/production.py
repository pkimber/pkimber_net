# -*- encoding: utf-8 -*-
from .base import *

DEBUG = False
TESTING = get_env_variable_bool('TESTING')

if get_env_variable_bool('SSL'):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [get_env_variable('ALLOWED_HOSTS'), ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{}_test'.format(SITE_NAME) if TESTING else SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': get_env_variable('DB_IP'),
        'PORT': '',
    }
}

# Celery
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# https://kfalck.net/2013/02/21/run-multiple-celeries-on-a-single-redis
CELERY_DEFAULT_QUEUE = '{}'.format(SITE_NAME)

from celery.schedules import crontab
CELERYBEAT_SCHEDULE = {
    'update_search_index': {
        'task': 'search.tasks.update_search_index',
        'schedule': crontab(minute='15', hour='*/1'),
    },
}

# mandrill
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MAIL_TEMPLATE_TYPE = 'mandrill'
MANDRILL_API_KEY = get_env_variable('MANDRILL_API_KEY')
MANDRILL_USER_NAME = get_env_variable('MANDRILL_USER_NAME')

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

HAYSTACK_CONNECTIONS = {
    'default': {
        'BATCH_SIZE': 100,
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'INDEX_NAME': '{}'.format(SITE_NAME),
        'TIMEOUT': 60 * 5,
        'URL': 'http://127.0.0.1:9200/',
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'celery_haystack.signals.CelerySignalProcessor'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = get_env_variable("SENDFILE_ROOT")
SENDFILE_URL = '/private'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)
