# events/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'f_name', 'm_name', 'l_name', 'email', 'birthday', 'password1', 'password2']

# events/forms.py

from django import forms
from .models import LocationsVenue

class VenueForm(forms.ModelForm):
    class Meta:
        model = LocationsVenue
        fields = ['address', 'l_owner', 'l_name', 'city', 'province_state', 'country']
