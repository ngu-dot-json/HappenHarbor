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

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

class ChangePasswordView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('account')  # Update with the name of your account view

class ChangeUsernameView(UpdateView):
    model = User
    template_name = 'change_username.html'
    fields = ['username']
    success_url = reverse_lazy('account')  # Update with the name of your account view


def about(request):
    foo = "bar"

    return render(request, 'events/about.html', {})

def account(request):
    foo = "bar"

    return render(request, 'events/account.html', {})


# Import data from Django Database
def all_events(request):
    event_list = Event.objects.all()

    return render(request, 'events/event_list.html',
        {'event_list': event_list
         
         })


def home(request):
    foo = "bar"
    return render(request, 'events/home.html', {})


def groups(request):
    foo = "bar"

    return render(request, 'events/groups.html', {})

def venues(request):
    foo = "bar"

    return render(request, 'events/venues.html', {})

def vendors(request):
    foo = "bar"

    return render(request, 'events/vendors.html', {})

def guests(request):
    foo = "bar"

    return render(request, 'events/guests.html', {})



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
            return redirect('/profile') #profile
        else:
            msg = 'Sign In Error'
            form = AuthenticationForm(request.POST)
            return render(request, 'events/signin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'events/signin.html', {'form': form})
  

def profile(request): 
    return render(request, 'events/profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')