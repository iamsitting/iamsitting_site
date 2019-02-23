from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iamsitting_site',
        'USER': 'iamsitting',
        'PASSWORD': 'iamsitting94',
        'HOST': 'localhost',
        'PORT': '',
      }
}

STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
