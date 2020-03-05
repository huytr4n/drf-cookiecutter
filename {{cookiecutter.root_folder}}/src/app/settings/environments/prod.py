import os
from app.settings.components.common import (
    INSTALLED_APPS,
    MIDDLEWARE,
)

# Turn off debugging
DEBUG = False

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

# Database configuration
DATABASES = {
    'default': {
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'ENGINE': 'django.db.backends.postgresql',
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': '',
    }
}
