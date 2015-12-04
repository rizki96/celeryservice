"""
Django settings for celeryservice project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zk!+8dqdzn^u&fv9j36x&@fozwe0!4!^xm3ex)nttv-pnits=i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'celeryservice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'celeryservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# celery settings
from kombu import Queue, Exchange

## Broker settings.
BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@localhost:5672')
#BROKER_URL = "amqp://guest:guest@localhost:5672/"
#BROKER_URL = os.getenv('BROKER_URL', 'redis://guest@localhost:6379')

#BROKER_HOST = "localhost"
#BROKER_PORT = 27017
#BROKER_TRANSPORT = 'mongodb'
#BROKER_VHOST = 'celery'

CELERY_DEFAULT_QUEUE = 'default'

CELERY_QUEUES = (
    Queue('default', exchange=Exchange('default', type='direct'),   routing_key='default'),
    #Queue('aws_uploads', exchange=Exchange('video', type='direct'), routing_key='video.uploads'),
)

CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_EXCHANGE_TYPE = 'direct'
CELERY_DEFAULT_ROUTING_KEY = 'default'

CELERY_IMPORTS = ('jobs.celery','jobs.sharedcelery',)
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'amqp')
#CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis')

#CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

## Using the database to store task state and results.
#CELERY_RESULT_BACKEND = "mongodb"
#CELERY_MONGODB_BACKEND_SETTINGS = {
#    "host": "localhost",
#    "port": 27017,
#    "database": "celery",
#    "taskmeta_collection": "celery_taskmeta",
#}