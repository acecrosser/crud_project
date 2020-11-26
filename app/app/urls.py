from django.conf.urls import url
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from auth.views import authentication_user

schema_view = get_schema_view(
   openapi.Info(
      title="API CRUD Project",
      default_version='v1',
      description="Решение тестового задания",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('user', include(('users.urls', 'users'), namespace='users')),
    path('api-token-auth', authentication_user)
]
