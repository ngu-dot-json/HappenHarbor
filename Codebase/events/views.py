# The default sign in, sign out and register system was adapted from: https://www.youtube.com/watch?v=6WnL0VHtPag

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .forms import *
from .models import *


def about(request):
    return render(request, 'events/about.html', {})

def account(request):
    user = request.user
    user2 = None

    if user.is_authenticated:
        try:
            user2 = User.objects.get(username=user.username)
        except User.DoesNotExist:
            pass

    return render(request, 'events/account.html', {'user': user, 'user2': user2})


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

            return redirect('account')
    else:
        auth_form = UserCreationForm()
        custom_form = CustomUserCreationForm()

    return render(request, 'events/signup.html', {'auth_form': auth_form, 'custom_form': custom_form})



# Code Adapted from Cairocoders' Tutorial on Django MySQL User Authentication Tutorial: https://www.youtube.com/watch?v=6WnL0VHtPag&t=4s
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
                return redirect('/account')
            else:
                msg = 'Sign In Error'
                return render(request, 'events/signin.html', {'msg': msg})
        else:
            msg = 'User does not exist'
            return render(request, 'events/signin.html', {'msg': msg})
    else:
        return render(request, 'events/signin.html', {'form': AuthenticationForm()})

def signout(request):
    logout(request)
    return redirect('/')


def add_venues(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():

            # Process the form data and set the owner before saving to the database
            venue = form.save(commit=False)
            user = request.user
            venue.l_owner = User.objects.get(username=user.username)
            venue.save()
            return redirect('venues')
    else:
        form = VenueForm()

    return render(request, 'events/add_venues.html', {'form': form})


def add_guests(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():

            # setting the new guests' ID to the next available Guest ID
            highest_guest_id = Guest.objects.aggregate(max_id=models.Max('guest_id'))['max_id']
            next_guest_id = 1 if highest_guest_id is None else highest_guest_id + 1
            form.instance.guest_id = next_guest_id
            form.save()
            
            return redirect('guests')
    else:
        form = GuestForm()

    return render(request, 'events/add_guests.html', {'form': form})




def add_vendors(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()

            vendors = form.save(commit=False)
            user = request.user
            userObj = User.objects.get(username=user.username)

            use = str(userObj.username)
            fnm = str(userObj.f_name)
            lnm = str(userObj.l_name)

            vendors.c_owner = fnm + " \"" + use + "\" "+ lnm
            vendors.save()

            return redirect('vendors')
    else:
        form = VendorForm()

    return render(request, 'events/add_vendors.html', {'form': form})


def add_groups(request):
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            user = request.user
            try:
                user_info = User.objects.get(username=user.username)
                user_group = form.save()
                PartOf.objects.create(group=user_group, username=user_info)

                return redirect('groups')
            except User.DoesNotExist:
                pass
    else:
        form = UserGroupForm()

    return render(request, 'events/add_groups.html', {'form': form})


def join_group(request, group_id):
    if request.user.is_authenticated:
        user = request.user
        group = get_object_or_404(UserGroups, group_id=group_id)

        # Check if the user is already a member of the group

        user_info = User.objects.get(username=user.username)


        if not PartOf.objects.filter(group=group, username=user_info).exists():
            # Add the user to the group
            PartOf.objects.create(group=group, username=user_info)

    # Redirect back to the groups page
    return redirect('groups')
