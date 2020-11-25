
from django.contrib import admin
from django.urls import path, include
from .views import index


urlpatterns = [
    path('', index),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('crud/', include(('crud.urls', 'crud'), namespace='crud')),
    path('admin/', admin.site.urls),
]
