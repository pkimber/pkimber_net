from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TESTING = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

TEMPLATE_STRING_IF_INVALID = '**** INVALID EXPRESSION: %s ****'

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
MEDIA_ROOT = 'media'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('127.0.0.1',)

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
