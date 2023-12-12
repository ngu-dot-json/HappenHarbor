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


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class AddEventForm(forms.ModelForm):
    guests = forms.ModelMultipleChoiceField(
        queryset=Guest.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Events
        fields = ['e_name', 'venue_add', 'e_site', 'e_desc', 'e_date', 'e_category', 'e_img', 'guests']

    def __init__(self, *args, **kwargs):
        super(AddEventForm, self).__init__(*args, **kwargs)
        self.fields['e_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['e_img'].widget.attrs['accept'] = 'image/*'  # Add this line to accept only image files

    def clean_e_img(self):
        image = self.cleaned_data.get('e_img', False)
        if image:
            if image.size > 4 * 1024 * 1024:  # 4MB limit
                raise forms.ValidationError("Image file size must be no more than 4 MB.")
            return image
        else:
            raise forms.ValidationError("Couldn't read uploaded image.")
