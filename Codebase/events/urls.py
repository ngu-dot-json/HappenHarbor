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

    path('add_venues', views.add_venues, name='add_venues'),
    path('add_guests', views.add_guests, name='add_guests'),
    path('add_vendors', views.add_vendors, name='add_vendors'),
    path('add_groups', views.add_groups, name='add_groups'),
    path('join_group/<int:group_id>/', views.join_group, name='join_group'),
    path('leave_group/<int:group_id>/', views.leave_group, name='leave_group'),
    path('add_events/', views.add_events, name='add_events'),
]
