from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetCompleteView

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
    path('signin/',views.signin, name='signin'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
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
    path('attended_events/', views.attended_events, name='attended_events'),
    path('attend_event/<int:event_id>/', views.attend_event, name='attend_event'),
    path('clear_attended_events/', views.clear_attended_events, name='clear_attended_events'),
    path('saved_events/', views.saved_events, name='saved_events'),
    path('save_event/<int:event_id>/', views.save_event, name='save_event'),
    path('clear_saved_events/', views.clear_saved_events, name='clear_saved_events'),
    ]
