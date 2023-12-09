# The default sign in, sign out and register system was adapted from: https://www.youtube.com/watch?v=6WnL0VHtPag

from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

def events(request):
    events = Events.objects.all()
    return render(request, 'events/events.html', {'events': events})

def vendors(request):
    vendors = Vendors.objects.all()
    return render(request, 'events/vendors.html', {'vendors': vendors})

def guests(request):
    guests = Guest.objects.all()
    return render(request, 'events/guests.html', {'guests': guests})

# CODE FOR SEARCH BAR
# def all_events(request):
#     query = request.GET.get('q', '')
#     search_field = request.GET.get('search_field', 'event_name')

#     if search_field == 'event_name':
#         events = Event.objects.filter(Q(name__icontains=query))
#     elif search_field == 'venue':
#         events = Event.objects.filter(Q(venue__name__icontains=query))
#     elif search_field == 'manager':
#         events = Event.objects.filter(Q(manager__icontains=query))
#     elif search_field == 'category':
#         events = Event.objects.filter(Q(event_type__icontains=query))
#     else:
#         events = Event.objects.all()

#     return render(request, 'events/event_list.html', {'event_list': events, 'query': query, 'search_field': search_field})












from django.shortcuts import render
from .models import Venue

from django.shortcuts import render
from django.db.models import Q
from .models import Venue

def list_venues(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'name')

    if search_field == 'name':
        venues = Venue.objects.filter(Q(name__icontains=query))
    elif search_field == 'address':
        venues = Venue.objects.filter(Q(address__icontains=query))
    elif search_field == 'phone':
        venues = Venue.objects.filter(Q(phone__icontains=query))
    else:
        venues = Venue.objects.all()

    context = {'venue_list': venues}
    return render(request, 'events/venue_list.html', context)





def about(request):
    return render(request, 'events/about.html', {})

def account(request):
    return render(request, 'events/account.html', {})

def home(request):
    return render(request, 'events/home.html', {})

def groups(request):
    return render(request, 'events/groups.html', {})

def venues(request):
    return render(request, 'events/venues.html', {})

def profile(request): 
    return render(request, 'events/profile.html')

# Code Adapted from Cairocoders' Tutorial on Django MySQL User Authentication Tutorial: https://www.youtube.com/watch?v=6WnL0VHtPag&t=4s
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'events/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'events/signup.html', {'form': form})

# Code Adapted from Cairocoders' Tutorial on Django MySQL User Authentication Tutorial: https://www.youtube.com/watch?v=6WnL0VHtPag&t=4s
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'events/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/account') #profile
        else:
            msg = 'Sign In Error'
            form = AuthenticationForm(request.POST)
            return render(request, 'events/signin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'events/signin.html', {'form': form})
  
def signout(request):
    logout(request)
    return redirect('/')