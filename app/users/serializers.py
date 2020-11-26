from rest_framework import serializers
from.models import User


class UserSerializers(serializers.ModelSerializer):

    data_create = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'data_create', 'last_login', 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}