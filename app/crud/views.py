from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Crud
from users.models import User
from users.serializers import UserSerializers
from .serializers import CrudSerializers


class CrudView(ListCreateAPIView):
    permission_classes = (AllowAny, )
    queryset = Crud.objects.all()
    serializer_class = CrudSerializers

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user_id'))
        return serializer.save(user=user)


class SingleCrudeView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializers

    queryset = Crud.objects.all()
    serializer_class = CrudSerializers
