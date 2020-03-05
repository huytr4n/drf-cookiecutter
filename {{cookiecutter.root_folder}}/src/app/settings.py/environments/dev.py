import os
from app.settings.components.common import (
    INSTALLED_APPS,
    MIDDLEWARE,
)
from app.settings.components import BASE_DIR

# development settings

DEBUG = True

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS += [
    'debug',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'NAME': os.environ.get('DATABASE_NAME', 'basedrf'),
        'USER': os.environ.get('DATABASE_USER', 'basedrf'),
        'ENGINE': 'django.db.backends.postgresql',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'basedrf'),
        'HOST': os.environ.get('DATABASE_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE_PORT', 5432),
    }
}

# No need whitelist, all origins will be accepted
CORS_ORIGIN_ALLOW_ALL = True
