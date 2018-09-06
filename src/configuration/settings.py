"""
Django settings for configuration project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import socket

ALLOWED_HOSTS = [
    "pirockinez.com",
]

DEPLOY_HOSTNAMES = [
    "anhel.in",
]

IS_DEPLOYED = socket.gethostname() in DEPLOY_HOSTNAMES

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "secret.txt"), mode="r", encoding="utf-8") as secret_file:
    SECRET_KEY = secret_file.readline().rstrip()

# SECURITY WARNING: don't run with debug turned on in production!
DEPLOYMENT_DEBUG = False
DEBUG = (not IS_DEPLOYED) or DEPLOYMENT_DEBUG

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home_page',
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

ROOT_URLCONF = 'configuration.urls'

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

WSGI_APPLICATION = 'configuration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if IS_DEPLOYED:
    from .production_datapase_config import DATABASES
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
if IS_DEPLOYED:
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
else:
    AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Novosibirsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
if IS_DEPLOYED:
    from .production_staticfiles_config import *
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static/")
    MEDIA_URL = STATIC_URL + "upload/"
    MEDIA_ROOT = os.path.join(STATIC_ROOT, "upload/")

if IS_DEPLOYED:
    SECURE_HSTS_SECONDS = 24 * 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_BROWSER_XSS_FILTER = True
