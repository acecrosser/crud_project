import jwt
from django.conf import settings
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from users.models import User


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authentication_user(request):
    print(request.data)
    try:
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user = User.objects.get(username=username, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as err:
                raise err

        else:
            res = {'error': 'Не получается авторизоваться'}
            return Response(res, status.HTTP_403_FORBIDDEN)

    except models.ObjectDoesNotExist:
        res = {'error': 'Введите корректную почту и пароль'}
        return Response(res)