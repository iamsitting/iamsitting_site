from .base import *

from utils import secrets

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.prod_secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = [secrets.ec2_public_ip, 'iamsitting.com']
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iamsitting_site',
        'USER': secrets.db_username,
        'PASSWORD': secrets.db_password,
        'HOST': 'localhost',
        'PORT': '',
      }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
