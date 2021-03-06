# Django settings for {{ project_name }} project.
from . import env_setting, local_join


ADMINS = (
    ('NAME', 'EMAIL'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_DOMAIN = '127.0.0.1:8000'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d %I:%M %p',     # '2006-10-25 02:30 PM'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y %I:%M %p',     # '10/25/2006 02:30 PM'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y %I:%M %p',     # '10/25/06 02:30 PM'
    '%m/%d/%y',              # '10/25/06'
)
DATETIME_FORMAT = 'D, M j, Y, P'
DATE_FORMAT = 'D, M j, Y'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = local_join('..', '_media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = local_join('..', '_static')
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.core.context_processors.tz',
    'django.core.context_processors.csrf',
    'django.contrib.messages.context_processors.messages',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    '{{ project_name }}.libs.common.middleware.PjaxMiddleware',
]

ATOMIC_REQUESTS = True

ROOT_URLCONF = '{{ project_name }}.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'rest_framework',
    '{{ project_name }}.libs.common',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = env_setting('{{ project_name|upper }}_SECRET_KEY', fail_if_missing=True)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(name)s [%(levelname)s] [%(module)s:%(funcName)s] %(message)s',
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'level': 'ERROR',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'INFO',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console',],
            'propagate': True,
        },
        '{{ project_name }}': {
            'handlers': ['console',],
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}

# Restframework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DATETIME_INPUT_FORMATS': list(DATETIME_INPUT_FORMATS) + ['iso-8601',],
    'UNICODE_JSON': True,
}

# Celery settings
BROKER_BACKEND = 'memory'
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_BACKEND = 'cache'
CELERY_CACHE_BACKEND = 'memory'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json',]

# Test Runner
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
