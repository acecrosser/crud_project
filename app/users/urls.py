from django.urls import path
from .views import UserRetrieveUpdateAPIView, UsersView

urlpatterns = [
    path('', UsersView.as_view()),
    path('<int:pk>', UserRetrieveUpdateAPIView.as_view()),
]