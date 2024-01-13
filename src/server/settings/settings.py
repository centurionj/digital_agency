import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCES_ROOT = BASE_DIR.parent

SECRET_KEY = get_random_secret_key()

DEBUG = os.getenv('DEBUG'),

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [os.getenv('DOMAIN'), 'http://localhost']

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cleanup',
    'ckeditor',
    'ckeditor_uploader',

    'server.about',
    'server.clients',
    'server.contacts',
    'server.documents',
    'server.landing',
    'server.portfolio',
    'server.projects',
    'server.workers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'server.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Database

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE'),
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': os.getenv('DB_PORT'),
#     }
# }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = os.getenv('TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CKEditor настройки

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = '/uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'autoGrow_bottomSpace': 10,
    },
}

# redis

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

# celery

CELERY_BROKER_URL = 'redis://{}:{}/0'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_RESULT_BACKEND = 'redis://{}:{}/0'.format(os.getenv('REDIS_HOST'), os.getenv('REDIS_PORT'))
CELERY_IMPORTS = ('customers.tasks', )
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Домен для сео

DOMAIN = os.getenv('DOMAIN')
