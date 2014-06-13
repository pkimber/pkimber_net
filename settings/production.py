from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

if get_env_variable_bool('SSL'):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [get_env_variable('ALLOWED_HOSTS'), ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'USER': SITE_NAME,
        'PASSWORD': get_env_variable('DB_PASS'),
        'HOST': get_env_variable('DB_IP'),
        'PORT': '',
    }
}

# FTP upload 'static' folder
FTP_STATIC_DIR = get_env_variable('FTP_STATIC_DIR')
FTP_STATIC_URL = get_env_variable('FTP_STATIC_URL')

HAYSTACK_CONNECTIONS = {
    'default': {
        'BATCH_SIZE': 100,
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'INDEX_NAME': '{}'.format(SITE_NAME),
        'TIMEOUT': 60 * 5,
        'URL': 'http://127.0.0.1:9200/',
    },
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.nginx'
SENDFILE_ROOT = get_env_variable("SENDFILE_ROOT")
SENDFILE_URL = '/private'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)

# django-mailgun
EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = get_env_variable("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = get_env_variable("MAILGUN_SERVER_NAME")
