from django.urls import path
from crud import views
from .views import CrudView, SingleCrudeView

urlpatterns = [
    path('', CrudView.as_view()),
    path('<int:pk>', SingleCrudeView.as_view()),
]