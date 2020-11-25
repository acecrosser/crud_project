from django.urls import path
from .views import CreateUserAPIView, authentication_user, UserRetrieveUpdateAPIView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('create/', csrf_exempt(CreateUserAPIView.as_view())),
    path('take_token/', authentication_user),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]