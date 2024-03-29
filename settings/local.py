# -*- encoding: utf-8 -*-
from .base import *

DEBUG = True
TESTING = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

HAYSTACK_CONNECTIONS = {
    "default": {"ENGINE": "haystack.backends.simple_backend.SimpleEngine"}
}

# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
MEDIA_ROOT = "media"

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('127.0.0.1',)

# https://django-sendfile2.readthedocs.io/en/
SENDFILE_BACKEND = "django_sendfile.backends.development"
SENDFILE_ROOT = BASE_DIR / "media-private"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
