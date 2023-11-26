from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

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