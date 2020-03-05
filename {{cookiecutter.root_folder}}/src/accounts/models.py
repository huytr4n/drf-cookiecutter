from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token # noqa

from django.db import models
from drf_core.models import create_api_key
from drf_core import fields


class User(AbstractUser):

    @property
    def is_user(self):
        return hasattr(self, 'role') and self.role in [self.USER_ROLE]

    @property
    def is_admin(self):
        return hasattr(self, 'role') and self.role in [self.ADMIN_ROLE]

    # define customize fields here.


# Automatically generates tastypie API key for the user.
models.signals.post_save.connect(create_api_key, sender=User)
