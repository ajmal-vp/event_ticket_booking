from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from event_app.filters import  EventFilter
from event_app.models import Customer, EventOwner, Event


@login_required(login_url='home')
def customer_details(request):
    data = Customer.objects.all()
    print(data)

    return render(request, "admin/customer_details.html", {"data": data})

@login_required(login_url='home')
def delete_customer(request,customer_id):
    data = Customer.objects.get(id=customer_id)
    print(data)
    data.delete()
    return redirect('customer_details')

def toggle_customer_status(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.is_active = not customer.is_active
    customer.save()
    return redirect('customer_details')

@login_required(login_url='home')
def EventOwner_details(request):
    data = EventOwner.objects.all()
    print(data)

    return render(request ,"admin/EventOwner_details.html" ,{"data" :data})

@login_required(login_url='home')
def delete_EventOwner(request,EventOwner_id):
    data = EventOwner.objects.get(id=EventOwner_id)
    print(data)
    data.delete()
    return redirect('EventOwner_details')

def toggle_EventOwner_status(request, EventOwner_id):
    event_owner = EventOwner.objects.get(id=EventOwner_id)
    event_owner.is_active = not event_owner.is_active
    event_owner.save()
    return redirect('EventOwner_details')

@login_required(login_url='home')
def events_list(request):
    queryset = Event.objects.all()
    event_filter = EventFilter(request.GET, queryset=queryset)
    filtered_events = event_filter.qs

    return render(request, "admin/events_list.html", {
        "data": filtered_events,
        "event_filter": event_filter
    })