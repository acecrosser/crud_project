from django.http import HttpResponse
from django.shortcuts import render
from users.views import authentication_user, CreateUserAPIView
from .form import RegistrationUser


def index(request):
    token = authentication_user(request)


def register_user(request):
    if request.method == 'POST':
        form = RegistrationUser(request.POST)
        create_user = CreateUserAPIView(form)
        return render(request, 'index.html', {'user': create_user})
    else:
        form = RegistrationUser()

    return render(request, 'app/index.html', {'form': form})

