# events/forms.py
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'f_name', 'm_name', 'l_name', 'email', 'birthday', 'password1', 'password2']



class VenueForm(forms.ModelForm):
    class Meta:
        model = LocationsVenue
        fields = ['address', 'l_owner', 'l_name', 'city', 'province_state', 'country']



class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['g_type', 'g_name', 'g_info']


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ['c_name', 'types_of_product', 'v_address', 'c_owner']


class UserGroupForm(forms.ModelForm):
    class Meta:
        model = UserGroups
        fields = ['ug_name', 'g_desc']
