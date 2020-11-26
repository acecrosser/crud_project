import jwt
from django.conf import settings
from django.shortcuts import render
from rest_framework_jwt.serializers import jwt_payload_handler

from .form import UpUser
from users.models import User
import json


def index(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=user, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_details = {}
            user_details['token'] = token
            return render(request, 'crud/index.html', {'token': user_details})
    form = UpUser
    return render(request, 'crud/index.html', {'form': form})


