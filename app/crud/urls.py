from django.urls import path
from crud.views import index


urlpatterns = [
    path('', index)
]