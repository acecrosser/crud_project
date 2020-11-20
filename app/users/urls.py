from django.conf.urls import url
from .views import CreateUserAPIView, authentication_user, UserRetrieveUpdateAPIView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^create/$', csrf_exempt(CreateUserAPIView.as_view())),
    url(r'^take_token/$', authentication_user),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
]