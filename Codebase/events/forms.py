# forms.py
from django import forms
from .models import LocationsVenue

class VenueForm(forms.ModelForm):
    class Meta:
        model = LocationsVenue
        fields = ['address', 'l_owner', 'l_name', 'city', 'province_state', 'country']
