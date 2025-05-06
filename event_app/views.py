from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, redirect

from event_app.forms import login_Form, Customer_login, EventOwner_login
from event_app.models import Event, EventOwner, Login, Booking


# Create your views here.

def home(request):
    return render(request, 'index.html')

@login_required(login_url='home')
def admin_dashboard(request):
    total_events = Event.objects.count()
    total_event_owners = EventOwner.objects.count()
    total_users = Login.objects.count()
    total_revenue = Event.objects.aggregate(total=Sum('price_per_ticket'))['total'] or 0
    recent_events = Event.objects.order_by('-event_date')[:5]

    return render(request, 'admin/admin_dashboard.html', {
        'total_events': total_events,
        'total_event_owners': total_event_owners,
        'total_users': total_users,
        'total_revenue': total_revenue,
        'recent_events': recent_events
    })

@login_required(login_url='home')
def EventOwner_dashboard(request):
    return render(request, 'EventOwner/eventowner_dashboard.html')

@login_required(login_url='home')
def customer_dashboard(request):
    return render(request, 'customer/customer_dashboard.html')

def customer_add(request):
    login_form1 = login_Form()
    customer_form = Customer_login()

    if request.method == 'POST':
        customer_form = Customer_login(request.POST)
        login_form1 = login_Form(request.POST)

        if customer_form.is_valid() and login_form1.is_valid():
            customer = login_form1.save(commit=False)
            customer.is_customer = True
            customer.save()
            user = customer_form.save(commit=False)
            user.customer_data = customer
            user.save()

            return redirect('login_views')

    return render(request,'customer/register.html',{'customer_form':customer_form,'login_form':login_form1})

def EventOwner_add(request):
    login_form2 = login_Form()
    EventOwner_form = EventOwner_login()

    if request.method == 'POST':
        EventOwner_form = EventOwner_login(request.POST)
        login_form2 = login_Form(request.POST)

        if EventOwner_form.is_valid() and login_form2.is_valid():
            EventOwner = login_form2.save(commit=False)
            EventOwner.is_EventOwner = True
            EventOwner.save()

            user = EventOwner_form.save(commit=False)
            user.event_owner_data = EventOwner
            user.save()

            return redirect('login_views')

    return render(request, 'EventOwner/EventOwner_login.html', {'EventOwner_form': EventOwner_form, 'login_form': login_form2})


def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password1')
        print(password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_dashboard')
            elif user.is_customer:
                return redirect('customer_dashboard')
            elif user.is_EventOwner:
                return redirect('EventOwner_dashboard')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,"login.html")


def logout_view(request):
    logout(request)
    return redirect('login_views')



