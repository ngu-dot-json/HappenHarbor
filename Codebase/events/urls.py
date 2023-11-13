from django.urls import path
from . import views

urlpatterns = [
    # Path Convertors
    # int: numbers
    # str: strings
    # path: whole URLS
    # slug: hyphen-and_underscore stuff
    # UUID: universually unique identifier

    path('', views.home, name="home"), # point to home function in views.py
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
]
