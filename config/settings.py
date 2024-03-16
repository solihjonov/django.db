"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-(&a9g)l$6c4s@ea(hcubipuww3n#be%uawi$k^h_-pkg_mtj#w')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

HOSTS = os.environ.get('ALLOWED_HOSTS')
ALLOWED_HOSTS = HOSTS.split(' ') if HOSTS else []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'blog',
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
]

# awesome_website/settings.py


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
url = 'postgres://back472_blog_user:G6BdUXUTjruB9deJPY6PGGBCxR4wmJNe@dpg-cno0qkn109ks73ch112g-a.oregon-postgres.render.com/back472_blog'
database_url = os.environ.get('DATABASE_URL', url)
DATABASES['default'] = dj_database_url.parse(database_url)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.registration.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.registration.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.registration.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.registration.password_validation.NumericPasswordValidator',
#     },
# ]

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

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'iamsolijonovasadbek@mail.com'
EMAIL_HOST_PASSWORD = 'qwerty002@#'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

LOGIN_REDIRECT_URL = "index"
LOGOUT_REDIRECT_URL = "index"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')
STATICFILES_DIRS = [BASE_DIR / 'blog/static']

MEDIA_URL = '/media/'  # new
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # new

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
