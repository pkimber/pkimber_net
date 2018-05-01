# -*- encoding: utf-8 -*-
"""
Django settings for app project.
"""
import os

# Normally you should not import ANYTHING from Django directly into your
# settings, but 'ImproperlyConfigured' is an exception.
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy


def get_env_variable(key):
    """
    Get the environment variable or return exception
    Copied from Django two scoops book
    """
    try:
        return os.environ[key]
    except KeyError:
        error_msg = "Set the {} env variable".format(key)
        print('ImproperlyConfigured: {}'.format(error_msg))
        raise ImproperlyConfigured(error_msg)


def get_env_variable_bool(key):
    """
    Retrieves env vars and makes Python boolean replacements
    Copied from:
    http://www.wellfireinteractive.com/blog/easier-12-factor-django/
    """
    result = get_env_variable(key)
    if result == 'True':
        result = True
    elif result == 'False':
        result = False
    else:
        error_msg = "The {} variable must be set to 'True' or "
        "'False': {}".format(key, result)
        print('ImproperlyConfigured: {}'.format(error_msg))
        raise ImproperlyConfigured(error_msg)
    return result


# We use the 'SITE_NAME' for the name of the database and the name of the
# cloud files container.
SITE_NAME = 'pkimber_net'

ADMINS = (
    ('pkimber', 'code@pkimber.net'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = 'web_static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_variable("SECRET_KEY")

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'elasticapm.contrib.django.middleware.TracingMiddleware',
    'reversion.middleware.RevisionMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'string_if_invalid': '**** INVALID EXPRESSION: %s ****',
        },
    },
]

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # admin after login, so we prefer login templates
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'captcha',
    # 'django_extensions',
    # 'debug_toolbar',
    'easy_thumbnails',
    'elasticapm.contrib.django',
    'mptt',
    'rest_framework',
    # http://www.django-rest-framework.org/api-guide/authentication#tokenauthentication
    'rest_framework.authtoken',
    'reversion',
    'sparkpost',
    'taggit',
)

LOCAL_APPS = (
    'base',
    'block',
    'compose',
    'contact',
    'crm',
    'dash',
    'enquiry',
    'finance',
    'invoice',
    'login',
    'mail',
    'project',
    'report',
    'search',
    'stock',
    'web',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

CONTACT_MODEL = 'contact.Contact'

DEFAULT_FROM_EMAIL = 'web@pkimber.net'

# sparkpost
EMAIL_BACKEND = "sparkpost.django.email_backend.SparkPostEmailBackend"
MAIL_TEMPLATE_TYPE = 'sparkpost'
SPARKPOST_API_KEY = get_env_variable('SPARKPOST_API_KEY')
SPARKPOST_OPTIONS = {
    'track_opens': False,
    'track_clicks': False,
    'transactional': True,
}

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('crm.ticket.home')

# Login URL. Used with login_required decorators when a user
# must be logged in before accessing the view otherwise this URL
# will be called.
# LOGIN_URL = reverse_lazy('login.login')

# https://github.com/praekelt/django-recaptcha
NOCAPTCHA = True
RECAPTCHA_PUBLIC_KEY = get_env_variable('NORECAPTCHA_SITE_KEY')
RECAPTCHA_PRIVATE_KEY = get_env_variable('NORECAPTCHA_SECRET_KEY')

# http://www.django-rest-framework.org/api-guide/authentication#tokenauthentication
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': True,
    # not sure if this is required or not
    # 'DATETIME_FORMAT': '%Y%m%dT%H%M%SZ',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
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
                'class': 'logging.NullHandler',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': "logger.log",
            'maxBytes': 500000,
            'backupCount': 10,
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
