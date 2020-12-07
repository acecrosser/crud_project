from .views import UsersViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='user')
urlpatterns = router.urls
