# The default sign in, sign out and register system was adapted from: https://www.youtube.com/watch?v=6WnL0VHtPag

from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash  # Add this line
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect




from django.db.models import Q

def all_events(request):
    query = request.GET.get('q', '')
    search_field = request.GET.get('search_field', 'event_name')

    if search_field == 'event_name':
        events = Event.objects.filter(Q(name__icontains=query))
    elif search_field == 'venue':
        events = Event.objects.filter(Q(venue__name__icontains=query))
    elif search_field == 'manager':
        events = Event.objects.filter(Q(manager__icontains=query))
    elif search_field == 'category':
        events = Event.objects.filter(Q(event_type__icontains=query))
    else:
        events = Event.objects.all()

    return render(request, 'events/event_list.html', {'event_list': events, 'query': query, 'search_field': search_field})


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

def guests(request):
    return render(request, 'events/guests.html', {})

def vendors(request):
    return render(request, 'events/vendors.html', {})

def profile(request): 
    return render(request, 'events/profile.html')
   

# shows default current month and year calendar
def calendar(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
    month = month.title() # Make first letter capital

    #convert month from name to num
    #month_num = int(list(calendar.month_name).index(month))
    month_num = 11

    # create a cealendar
    cal = HTMLCalendar().formatmonth(int(year), month_num)

    # get current year
    now = datetime.now()
    curr_year = now.year

    # get current time -- NOT MST MAYBE GWT?
    curr_time = now.strftime('%I:%M %p')

    return render(request,           
        'events/calendar.html', {
            "name": name,
            "year": year,
            "month": month,
            "month_num": month_num,
            "cal": cal,
            "curr_year": curr_year,
            "curr_time": curr_time,
        })

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