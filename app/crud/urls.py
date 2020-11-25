from django.urls import path
from .views import CrudView, SingleCrudeView

urlpatterns = [
    path('', CrudView.as_view()),
    path('<int:pk>', SingleCrudeView.as_view()),
]