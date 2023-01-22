from rest_framework import serializers


class UserPublicSerializers(serializers.Serializer):
    # All the fields below are part of the Django User model
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    is_active = serializers.CharField(read_only=True)
    is_anonymous = serializers.CharField(read_only=True)
    is_authenticated = serializers.CharField(read_only=True)
    is_staff = serializers.CharField(read_only=True)
    is_superuser = serializers.CharField(read_only=True)
    last_login = serializers.CharField(read_only=True)
