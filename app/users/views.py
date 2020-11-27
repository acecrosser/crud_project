from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import User
from .serializers import UserSerializers


class CreateUserAPIView(APIView):

    permission_classes = (AllowAny, )

    def post(self, request):
        user = request.data
        serializer = UserSerializers(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsersView(ListCreateAPIView):

    permission_classes = (AllowAny, )

    queryset = User.objects.all()
    serializer_class = UserSerializers


class UpdateUserAPIView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        data = request.data
        serializer = UserSerializers(user, data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        res = {'error': 'Не получается обновить данные'}
        return Response(res, status.HTTP_403_FORBIDDEN)


class DeleteUserAPIView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        if user:
            try:
                user.is_active = False
                user.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Exception as err:
                raise err

        res = {'error': 'Пользователь не найден'}
        return Response(res, status.HTTP_403_FORBIDDEN)


class UserRetrieveUpdateAPIView(RetrieveUpdateDestroyAPIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    queryset = User.objects.all()
    serializer_class = UserSerializers

