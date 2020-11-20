from rest_framework import serializers
from.models import User


class UserSerializers(serializers.ModelSerializer):

    data_create = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'data_create', 'password']
        extra_kwargs = {'password': {'write_only': True}}