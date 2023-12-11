# The default sign in, sign out and register system was adapted from: https://www.youtube.com/watch?v=6WnL0VHtPag

from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

def about(request):
    return render(request, 'events/about.html', {})

def account(request):
    return render(request, 'events/account.html', {})

def home(request):
    return render(request, 'events/home.html', {})


def vendors(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'c_name')

    if search_field == 'c_name':
        vendors = Vendors.objects.filter(Q(c_name__icontains=query))
    elif search_field == 'types_of_product':
        vendors = Vendors.objects.filter(Q(types_of_product__icontains=query))
    elif search_field == 'events':
        vendors = Vendors.objects.filter(hasvendors__event__e_name__icontains=query)
    else:
        vendors = Vendors.objects.all()

    return render(request, 'events/vendors.html', {'vendors': vendors, 'query': query, 'search_field': search_field})


def guests(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'g_name')

    if search_field == 'g_name':
        guests = Guest.objects.filter(Q(g_name__icontains=query))
    elif search_field == 'g_type':
        guests = Guest.objects.filter(Q(g_type__icontains=query))
    elif search_field == 'attending':
        guests = Guest.objects.filter(hasguests__event__e_name__icontains=query)
    else:
        guests = Guest.objects.all()

    return render(request, 'events/guests.html', {'guests': guests, 'query': query, 'search_field': search_field})


def events(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'event_name')

    if search_field == 'event_name':
        events = Events.objects.filter(Q(e_name__icontains=query))
    elif search_field == 'venue':
        events = Events.objects.filter(Q(venue_add__l_name__icontains=query))
    elif search_field == 'organizer':
        events = Events.objects.filter(Q(org_username__icontains=query))
    elif search_field == 'category':
        events = Events.objects.filter(Q(e_category__icontains=query))
    elif search_field == 'guest':
        events = Events.objects.filter(Q(hasguests__guest__g_name__icontains=query))
    else:
        events = Events.objects.all()

    return render(request, 'events/events.html', {'events': events, 'query': query, 'search_field': search_field})


def groups(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'ug_name')

    if search_field == 'ug_name':
        usergroups = UserGroups.objects.filter(ug_name__icontains=query)
    elif search_field == 'group_member':
        usergroups = UserGroups.objects.filter(partof__username__username__icontains=query)
    else:
        usergroups = UserGroups.objects.all()

    return render(request, 'events/groups.html', {'usergroups': usergroups, 'query': query, 'search_field': search_field})


def venues(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'l_name')

    if search_field == 'l_name':
        venues = LocationsVenue.objects.filter(Q(l_name__icontains=query))
    elif search_field == 'city':
        venues = LocationsVenue.objects.filter(Q(city__icontains=query))
    elif search_field == 'province_state':
        venues = LocationsVenue.objects.filter(Q(province_state__icontains=query))
    elif search_field == 'country':
        venues = LocationsVenue.objects.filter(Q(country__icontains=query))
    elif search_field == 'events':
        venues = LocationsVenue.objects.filter(isat__event__e_name__icontains=query)
    else:
        venues = LocationsVenue.objects.all()

    return render(request, 'events/venues.html', {'venues': venues, 'query': query, 'search_field': search_field})


# Code Adapted from Cairocoders' Tutorial on Django MySQL User Authentication Tutorial: https://www.youtube.com/watch?v=6WnL0VHtPag&t=4s
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from datetime import datetime

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        auth_form = UserCreationForm(request.POST)
        custom_form = CustomUserCreationForm(request.POST)

        if auth_form.is_valid() and custom_form.is_valid():
            # Save user in the default auth_user table
            auth_user = auth_form.save()

            # Create a user in the custom User table
            user = custom_form.save(commit=False)
            user.username = auth_user.username
            user.save()

            # Authenticate and log in the user
            user_auth = authenticate(request, username=auth_user.username, password=auth_form.cleaned_data.get('password1'))
            login(request, user_auth)

            print("Redirecting to additional_info")
            return redirect('additional_info')  # Redirect to additional_info template
        else:
            print("Forms are not valid:", auth_form.errors, custom_form.errors)
    else:
        auth_form = UserCreationForm()
        custom_form = CustomUserCreationForm()

    return render(request, 'events/signup.html', {'auth_form': auth_form, 'custom_form': custom_form})







# Code Adapted from Cairocoders' Tutorial on Django MySQL User Authentication Tutorial: https://www.youtube.com/watch?v=6WnL0VHtPag&t=4s
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import User

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'events/home.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is None or password is None:
            msg = 'Invalid Form Submission'
            return render(request, 'events/signin.html', {'msg': msg})

        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/account')  # Redirect to profile or desired page
            else:
                msg = 'Sign In Error'
                return render(request, 'events/signin.html', {'msg': msg})
        else:
            msg = 'User does not exist'
            return render(request, 'events/signin.html', {'msg': msg})
    else:
        return render(request, 'events/signin.html', {'form': AuthenticationForm()})


def additional_info(request):
    # You may want to add logic to check if the user is authenticated or has already filled out the additional info form
    return render(request, 'events/additional_info.html')

def signout(request):
    logout(request)
    return redirect('/')