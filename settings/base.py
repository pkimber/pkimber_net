"""
Django settings for app project.
"""
import os

# Normally you should not import ANYTHING from Django directly into your
# settings, but 'ImproperlyConfigured' is an exception.
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy


def get_env_variable(key):
    """
    Get the environment variable or return exception
    Copied from Django two scoops book
    """
    try:
        return os.environ.get(key)
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

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

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

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # admin after login, so we prefer login templates
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    # 'django_extensions',
    # 'debug_toolbar',
    'easy_thumbnails',
    'haystack',
    'mailgun_incoming',
    'reversion',
    'south',
)

LOCAL_APPS = (
    'project',
    'base',
    'block',
    'crm',
    'invoice',
    'login',
    'search',
    'web',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('project.home')

# Login URL. Used with login_required decorators when a user
# must be logged in before accessing the view otherwise this URL
# will be called.
# LOGIN_URL = reverse_lazy('login.login')

# This project is not using Haystack/SOLR, but the cron task will still be
# running... so just install the simple engine.
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
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
