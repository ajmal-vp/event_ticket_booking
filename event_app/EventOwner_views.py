from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import EventOwner, Event, Booking, Login
from event_app.forms import EventForm, EventOwner_login
from event_app.models import EventOwner, Event

@login_required(login_url='home')
def event_upload(request):

    user_data = request.user
    EventOwner_data = EventOwner.objects.get(event_owner_data=user_data)

    if request.method == 'POST':

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            obj =  form.save(commit=False)
            obj.event_owner = EventOwner_data
            obj.save()
            return redirect("event_details")
    else:
        form = EventForm()
    return render(request, 'EventOwner/event_upload.html', {'form': form})

@login_required(login_url='home')
def event_details(request):

    user = request.user
    EventOwner_data1 = EventOwner.objects.get(event_owner_data = user)
    data = Event.objects.filter(event_owner = EventOwner_data1)

    return render(request,"EventOwner/view_events.html",{"data":data})

@login_required(login_url='home')
def update_events(request,id):
    data = Event.objects.get(id=id)

    form1 = EventForm(instance=data)


    if request.method == 'POST':
        data = EventForm(request.POST,instance= data)
        if data.is_valid():
            data.save()
            return redirect("event_details")

    return render(request,"EventOwner/update_events.html",{"Event_Form":form1})

@login_required(login_url='home')
def delete_events(request,id):
    data = Event.objects.get(id=id)
    data.delete()
    return redirect('event_details')



@login_required(login_url='home')
def payment_tracking(request):

    event_owner = EventOwner.objects.get(event_owner_data=request.user)
    events = Event.objects.filter(event_owner=event_owner)
    bookings = Booking.objects.filter(event__in=events, payment_status=True)
    total_earnings = sum(b.tickets_booked * float(b.event.price_per_ticket) for b in bookings)

    return render(request, 'EventOwner/payment_tracking.html', {
        'bookings': bookings,
        'total_earnings': total_earnings
    })

@login_required(login_url='home')
def event_owner_profile(request):
    user = request.user
    eventOwner = Login.objects.get(id=user.id)
    return render(request, 'EventOwner/event_owner_profile.html', {'eventOwner': eventOwner})