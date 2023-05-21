"""
Django settings for AIESL project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == '1'
ENV_ALLOWED_HOST = os.environ.get("ENV_ALLOWED_HOST")
ALLOWED_HOSTS = ["146.190.9.34"]
if ENV_ALLOWED_HOST:
    ALLOWED_HOSTS = [ ENV_ALLOWED_HOST ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myaieslapp'
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

ROOT_URLCONF = 'AIESL.urls'

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

WSGI_APPLICATION = 'AIESL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': BASE_DIR / 'db.mysql',
#     }
# }

DB_USERNAME = os.environ.get("MYSQL_USER")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_DATABASE = os.environ.get("MYSQL_DB")
DB_HOST = os.environ.get("MYSQL_HOST")
DB_PORT = os.environ.get("MYSQL_PORT")
DB_IS_AVAIL = all( [  # to make sure all these are set
    DB_USERNAME,
    DB_PASSWORD, # to configure all thses as needed
    DB_DATABASE, 
    DB_HOST, 
    DB_PORT
])
DB_IGNORE_SSL=os.environ.get("DB_IGNORE_SSL")=="true"


if DB_IS_AVAIL: # and POSTGRES_READY:
    DATABASES = {
        "default": {
            "ENGINE": "mysql.connector.django",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME, 
            "PASSWORD": DB_PASSWORD, 
            "HOST": DB_HOST, 
            "PORT": DB_PORT,
            'OPTIONS': {
              'auth_plugin': 'mysql_native_password',
        }

            
        }
    }
    


    if not DB_IGNORE_SSL:
        DATABASES["default"]["OPTIONS"] = {
            "sslmode": "require"
        }

print(DATABASES)

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [
    os.path.join(BASE_DIR, 'static')
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL= "mainpage"