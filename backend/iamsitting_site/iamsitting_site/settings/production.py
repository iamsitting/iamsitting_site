from utils import secrets

from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.prod_secret

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
SSL_ON = True

# ALLOWED_HOSTS = [secrets.ec2_public_ip, 'iamsitting.com']
ALLOWED_HOSTS = ['*']

# Email setup
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = secrets.email_user
EMAIL_HOST_PASSWORD = secrets.email_pass

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': secrets.db_name,
    'USER': secrets.db_username,
    'PASSWORD': secrets.db_password,
    'HOST': secrets.db_host,
    'PORT': secrets.db_port,
  }
}

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (

)

if SSL_ON:
  SESSION_COOKIE_SECURE = True
  SESSION_COOKIE_HTTPONLY = True
  SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
  SECURE_SSL_REDIRECT = True

# Logging Configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'feedback': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/feedback.log"),
        },
        'user_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "logs/debug.log"),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['feedback'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'debugger': {
            'handlers': ['user_debug', 'feedback'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security.csrf': {
            'handlers': ['feedback'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
