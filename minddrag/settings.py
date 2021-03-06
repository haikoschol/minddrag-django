import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]

# ==============================================================================
# debug settings
# ==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ()
if DEBUG:
    TEMPLATE_STRING_IF_INVALID = ''

# ==============================================================================
# cache settings
# ==============================================================================

CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME
CACHE_MIDDLEWARE_SECONDS = 600

# ==============================================================================
# email and error-notify settings
# ==============================================================================

ADMINS = (
    ('Haiko Schol', 'hs@zeropatience.net'),
)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'minddrag@zeropatience.net'
SERVER_EMAIL = 'error-notify@zeropatience.net'

EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'minddrag@interwebatron24.de'
EMAIL_HOST_PASSWORD = 'ijvavDotnamoadcakHyk'
EMAIL_USE_TLS = True

# ==============================================================================
# auth settings
# ==============================================================================

# put all login/registration/profile stuff under one url prefix
ACCOUNTS_URL_PREFIX='/accounts/'

LOGIN_URL = ACCOUNTS_URL_PREFIX + 'login/'
LOGOUT_URL = ACCOUNTS_URL_PREFIX + 'logout/'
LOGIN_REDIRECT_URL = '/'

# ==============================================================================
# database settings
# ==============================================================================

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'dev.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# ==============================================================================
# i18n and url settings
# ==============================================================================

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
LANGUAGES = (('en', 'English'),
             ('de', 'German'))
USE_I18N = True

SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/django_admin_media/'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# ==============================================================================
# application and middleware settings
# ==============================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django_extensions',
    'registration',
    #'south',
    'minddrag.core',
    'minddrag.api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
#    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
)

# ==============================================================================
# the secret key
# ==============================================================================

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to \
generate your secret key!' % SECRET_FILE)

# ==============================================================================
# third party
# ==============================================================================

# django-registration

ACCOUNT_ACTIVATION_DAYS = 7

# django-piston

PISTON_EMAIL_ERRORS = False
PISTON_DISPLAY_ERRORS = True
PISTON_STREAM_OUTPUT = False

# ==============================================================================
# host specific settings
# ==============================================================================

try:
    from local_settings import *
except ImportError:
    pass

