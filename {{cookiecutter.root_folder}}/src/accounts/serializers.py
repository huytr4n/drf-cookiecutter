from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """UserSerializer"""

    class Meta:
        """Meta"""

        model = User
        fields = '__all__'


class AuthenticateSerializer(UserSerializer):
    """AuthenticateSerializer"""

    full_name = serializers.SerializerMethodField()

    class Meta:
        """Meta"""

        model = User
        fields = ['id', 'username', 'password', 'auth_token', 'full_name', ]
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    def get_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)
