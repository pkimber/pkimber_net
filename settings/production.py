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
        'HOST': '',                                             # Set to empty string for localhost. Not used with sqlite3.
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
        'stderr': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['stderr'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = get_env_variable("MEDIA_ROOT")

# We want attachments to be stored in a private location and NOT available to
# the world at a public URL.  The idea for this came from:
# http://nemesisdesign.net/blog/coding/django-private-file-upload-and-serving/
MEDIA_ROOT_PRIVATE = get_env_variable("MEDIA_ROOT_PRIVATE")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('87.115.141.255',)
