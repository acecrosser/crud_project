from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializers


class CreateUserAPIView(APIView):

    permission_classes = (AllowAny, )

    def post(self, request):
        user = request.data
        serializer = UserSerializers(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
