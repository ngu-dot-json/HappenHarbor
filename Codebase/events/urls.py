from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), # point to home function in views.py
]
