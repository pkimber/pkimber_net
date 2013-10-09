from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

if get_env_variable_bool('SSL'):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = [get_env_variable('DOMAIN'), ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',     # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': SITE_NAME,                                      # Or path to database file if using sqlite3.
        'USER': SITE_NAME,                                      # Not used with sqlite3.
        'PASSWORD': get_env_variable('DB_PASS'),                # Not used with sqlite3.
        'HOST': get_env_variable('DB_IP'),                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                             # Set to empty string for default. Not used with sqlite3.
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
                'class':'django.utils.log.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
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
