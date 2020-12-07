from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):

    data_create = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'data_create', 'last_login', 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
