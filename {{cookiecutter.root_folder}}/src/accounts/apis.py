from django.contrib.auth import authenticate
from drf_core import apis, apidoc
from accounts.serializers import AuthenticateSerializer


class LoginView(apis.BaseFunctionView):
    """
    Single function view for login API
    """

    resource_name = ''

    @apidoc.swagger_auto_schema(
        responses={200: 'OK'},
        manual_parameters=[
            apidoc.Parameter(
                'username',
                apidoc.IN_QUERY,
                description='Username',
                type=apidoc.TYPE_STRING,
                required=True,
            ),
            apidoc.Parameter(
                'password',
                apidoc.IN_QUERY,
                description='Password',
                type=apidoc.TYPE_STRING,
                format=apidoc.FORMAT_PASSWORD,
                required=True,
            )
        ]
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return self.bad_request(message='Can not authenticate user', code=400)

        # get user data.
        user_data = AuthenticateSerializer(user)

        return self.create_response(user_data.data)


class LogoutView(apis.BaseFunctionView):
    """
    Single function view for logout API.
    """

    @apis.authentication_classes((apis.SessionAuthentication, apis.TokenAuthentication))
    @apis.permission_classes((apis.IsAuthenticated,))
    def get(self, request, format=None):
        """
        Log out API
        """
        if not request.user.pk:
            return self.bad_request(message='You are not logged in', code=400)

        return self.create_response()


# define all routers
apps = []
