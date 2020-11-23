from rest_framework import serializers
from .models import Crud


class CrudSerializers(serializers.ModelSerializer):

    date = serializers.ReadOnlyField()

    class Meta(object):
        model = Crud
        fields = ['id', 'title', 'body', 'user_id', 'date']
