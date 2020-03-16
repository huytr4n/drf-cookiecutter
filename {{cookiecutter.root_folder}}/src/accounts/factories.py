import os

from drf_core import factories
from .models import User
from django.contrib.auth.hashers import make_password

PASSWORD = os.environ.get('ADMIN_PASSWORD', '123456')
DOMAIN = os.environ.get('ADMIN_DOMAIN', 'domain.com')

test_password = make_password(PASSWORD)


# =============================================================================
# User
# =============================================================================
class UserFactory(factories.ModelFactory):
    """
    Faker for User model.

    See https://docs.djangoproject.com/en/dev/ref/contrib/auth/#user
    for details.
    """

    first_name = factories.Sequence(lambda n: 'User_%d' % n)
    last_name = 'Doe'
    password = test_password

    @factories.lazy_attribute
    def username(self):
        # Makes the first user in the sequence makes more beautiful.
        # For example, admin_0 becomes just admin.
        username = self.first_name.lower()
        if username.endswith('_0'):
            username = username[:-2]

        return username

    email = factories.LazyAttribute(
        lambda user: '%s@%s' % (
            user.username,
            DOMAIN
        )
    )

    class Meta:
        """Meta"""

        model = User
        django_get_or_create = ('username',)


class SuperUserFactory(UserFactory):
    """SuperUserFactory"""

    first_name = factories.Sequence(lambda n: 'Admin_%d' % n)
    last_name = 'User'
    is_staff = True
    is_superuser = True
    password = test_password

apps = [
    UserFactory,
    SuperUserFactory,
]
