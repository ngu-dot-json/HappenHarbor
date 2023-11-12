from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime



def home(request, year, month):
    name = "John"
    month = month.title() # Make first letter capital

    #convert month from name to num
    month_num = int(list(calendar.month_name).index(month))

    # create a cealendar
    cal = HTMLCalendar().formatmonth(int(year), month_num)

    # get current year
    now = datetime.now()
    curr_year = now.year

    # get current time -- NOT MST MAYBE GWT?
    curr_time = now.strftime('%I:%M %p')


    return render(request,           
        'home.html', {
            "name": name,
            "year": year,
            "month": month,
            "month_num": month_num,
            "cal": cal,
            "curr_year": curr_year,
            "curr_time": curr_time,
        })