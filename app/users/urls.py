from django.conf.urls import url
from .views import CreateUserAPIView

urlpatterns = [
    url(r'^create/$', CreateUserAPIView)
]