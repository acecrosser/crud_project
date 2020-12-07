from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializers


class UsersViewSet(ViewSet, ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request):
        user = request.data
        serializer = UserSerializers(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response({'users': serializer.data})

    def retrieve(self, request, pk):
        users = User.objects.all()
        user = get_object_or_404(users, pk=pk)
        serializer = UserSerializers(user)
        return Response(serializer.data)

    def update(self, request, pk):
        user = User.objects.get(id=pk)
        data = request.data
        serializer = UserSerializers(user, data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        res = {'error': 'Не получается обновить данные'}
        return Response(res, status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, pk):
        user = User.objects.get(id=pk)
        data = request.data
        print(data)
        serializer = UserSerializers(user, data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        res = {'error': 'Не получается обновить данные'}
        return Response(res, status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk):
        user = User.objects.get(id=pk)
        if user:
            user.is_active = False
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        res = {'error': 'Пользователь не найден'}
        return Response(res, status.HTTP_403_FORBIDDEN)
