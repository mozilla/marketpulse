"""
Django settings for marketpulse project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

import dj_database_url
from decouple import Csv, config


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

TEMPLATE_DEBUG = config('DEBUG', default=DEBUG, cast=bool)

SITE_URL = config('SITE_URL')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Name of the top-level module where all the apps live.
PROJECT_MODULE = 'marketpulse'

# Application definition

INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'django_browserid',
    'django_nose',
    'import_export',
    'django_countries',

    # Project specific apps
    '%s.auth' % PROJECT_MODULE,
    '%s.base' % PROJECT_MODULE,
    '%s.main' % PROJECT_MODULE,
    '%s.devices' % PROJECT_MODULE,
    '%s.geo' % PROJECT_MODULE,
]

for app in config('EXTRA_APPS', default='', cast=Csv()):
    INSTALLED_APPS.append(app)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

ROOT_URLCONF = '%s.urls' % PROJECT_MODULE

WSGI_APPLICATION = '%s.wsgi.application' % PROJECT_MODULE


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        cast=dj_database_url.parse
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en-us')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = config('USE_I18N', default=True, cast=bool)

USE_L10N = config('USE_L10N', default=True, cast=bool)

USE_TZ = config('USE_TZ', default=True, cast=bool)

STATIC_ROOT = config('STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
STATIC_URL = config('STATIC_URL', '/static/')

MEDIA_ROOT = config('MEDIA_ROOT', default=os.path.join(BASE_DIR, 'media'))
MEDIA_URL = config('MEDIA_URL', '/files/')

SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=not DEBUG, cast=bool)

TEMPLATE_LOADERS = (
    'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

JINGO_EXCLUDE_APPS = ['browserid', 'admin']

# Django-CSP
CSP_DEFAULT_SRC = (
    "'self'",
    'https://login.persona.org',
    'https://*.tiles.mapbox.com',
    'https://*.cloudfront.net',
)
CSP_FONT_SRC = (
    "'self'",
    'http://*.mozilla.net',
    'https://*.mozilla.net'
)
CSP_IMG_SRC = (
    "'self'",
    'data:',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://*.tiles.mapbox.com',
)
CSP_SCRIPT_SRC = (
    "'self'",
    'http://www.mozilla.org',
    'https://www.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://login.persona.org',
    'https://*.mapbox.com',
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    'http://www.mozilla.org',
    'https://www.mozilla.org',
    'http://*.mozilla.net',
    'https://*.mozilla.net',
    'https://*.mapbox.com',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Django-browserid settings
AUTH_USER_MODEL = 'mozillians_auth.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           '%s.auth.backend.MozilliansAuthBackend' % PROJECT_MODULE)
BROWSERID_VERIFY_CLASS = '%s.auth.views.BrowserIDVerify' % PROJECT_MODULE

BROWSERID_AUDIENCES = config('BROWSERID_AUDIENCES', cast=Csv())
LOGIN_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL_FAILURE = '/'
LOGIN_URL = '/'
BROWSERID_REQUEST_ARGS = {
    'siteName': config('BROWSERID_SITENAME', default=PROJECT_MODULE),
    'siteLogo': config('BROWSERID_SITELOGO', default=None)
}

# Mozillians.org API settings
MOZILLIANS_API_URL = config('MOZILLIANS_API_URL', default=None)
MOZILLIANS_API_KEY = config('MOZILLIANS_API_KEY', default=None)
MOZILLIANS_APP_NAME = config('MOZILLIANS_APP_NAME', default=None)

# Mapbox API
MAPBOX_GEOCODE_URL = 'https://api.tiles.mapbox.com/v4/geocode/mapbox.places/'
MAPBOX_MAP_ID = config('MAPBOX_MAP_ID', default=None)
MAPBOX_TOKEN = config('MAPBOX_TOKEN', default=None)
