from drf_core.tests import BaseTestCase

from accounts.apis import LoginView
from accounts.models import User
from accounts.factories import UserFactory


class AccountViewSetTestCase(BaseTestCase):
    resource = LoginView

    def test_assert_ok(self):
        self.assertEqual(True, True)

    def test_login_ok(self):
        data = {
            'username': 'user',
            'password': '123456'
        }

        self.post_json_ok(data=data, fragment='login/')

    def test_login_wrong_password(self):
        data = {
            'username': 'user',
            'password': '1234567'
        }

        self.post_json_bad_request(data=data, fragment='login/')

    def test_logout_ok(self):
        self.get_json_ok('logout/')

    def test_logout_forbidden(self):
        # Give the logout request no token header.
        # Expect the method is forbidden.
        self.auth = None
        self.get_json_method_forbidden('logout/')
