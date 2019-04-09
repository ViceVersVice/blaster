"""
Django settings for GG project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('GG//pss.txt') as f:
    s_key = f.read().strip()


SECRET_KEY = s_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ["192.168.1.3", "localhost",]


# Application definition

INSTALLED_APPS = [
    'rest_framework.authtoken',
    'rest_framework',
    'blaster.apps.BlasterConfig',
    'user_managment.apps.UserManagmentConfig',
    'comment.apps.CommentConfig',
    'A.apps.AConfig',
    'widget_tweaks',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_managment.middleware.LastActivity',

]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
    'UNAUTHENTICATED_TOKEN': None,
}

ROOT_URLCONF = 'GG.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'GG.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
with open('GG//db_pss.txt') as f:
    db_pswrd = f.read().strip()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Blaster',
        'USER': 'postgres',
        'PASSWORD': str(db_pswrd),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
#email smtp

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
DEFAULT_FROM_EMAIL = 'blaster.inf.tool@gmail.com'
EMAIL_HOST_USER = 'blaster.inf.tool@gmail.com'
with open('GG//pss2.txt') as f:
    psswrd = f.read().strip()
EMAIL_HOST_PASSWORD = psswrd
EMAIL_PORT = 587

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#for deployment
#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static_root/'
MEDIA_URL = "/media/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
TEST_ROOT = os.path.join(BASE_DIR, 'blaster/tool') # root for user sequence files input
