from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_params),
    path('get_params', views.get_params),
]