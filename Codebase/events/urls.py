from django.urls import path
# from django.contrib import admin
from . import views

from django.urls import path
# from .views import ChangePasswordView, ChangeUsernameView


urlpatterns = [
    # Path Convertors
    # int: numbers
    # str: strings
    # path: whole URLS
    # slug: hyphen-and_underscore stuff
    # UUID: universually unique identifier

    path('', views.home, name="home"), # point to home function in views.py
    path('events/', views.events, name='events'),    
    path('about', views.about, name="about"),
    path('account', views.account, name="account"),
    path('groups', views.groups, name="groups"),
    # path('admin', admin.site.urls),
    path('signin/',views.signin, name='signin'),
    path('signout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),
    path('venues/', views.venues, name='venues'),
    path('vendors/', views.vendors, name='vendors'),
    path('guests', views.guests, name='guests'),
    path('add_venue/', views.add_venue, name='add_venue'),
]
