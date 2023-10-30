from django.urls import path
from . import views

urlpatterns = [
    path('', views.validate_pesel, name='validate_pesel'),
]
