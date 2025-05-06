from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .filters import CategoryFilter
from .models import Event, Booking, Login
from .forms import BookingForm
from django.contrib import messages

@login_required(login_url='home')
def event_list(request):
    events = Event.objects.all()
    myFilter = CategoryFilter(request.GET, queryset=events)
    events = myFilter.qs

    return render(request, 'Customer/events_list.html', {'data': events, 'myFilter': myFilter})

@login_required(login_url='home')
def book_now(request, event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        tickets_booked = int(request.POST.get('tickets_booked'))

        if tickets_booked <= event.total_tickets:

            request.session['event_id'] = event.id
            request.session['tickets_booked'] = tickets_booked

            return redirect('card_payment', event_id=event.id)
        else:
            messages.error(request, 'Not enough tickets available.')

    return render(request, 'customer/book_now.html', {'event': event})

@login_required(login_url='home')
def payment_page(request, event_id):
    event_id = request.session.get('event_id')
    tickets_booked = request.session.get('tickets_booked')

    if not event_id or not tickets_booked:
        messages.error(request, "No booking information found.")
        return redirect('event_list')

    event = Event.objects.get(id=event_id)

    total_price = int(tickets_booked) * float(event.price_per_ticket)

    return render(request, 'customer/payment_page.html', {
        'event': event,
        'tickets_booked': tickets_booked,
        'total_price': total_price,
    })
@login_required(login_url='home')
def card_payment(request, event_id):
    event = Event.objects.get(id=event_id)
    tickets_booked = int(request.session.get('tickets_booked'))

    if request.method == 'POST':
        # Redirect to payment success page after "fake" payment
        return redirect('payment_success')

    return render(request, 'customer/card_payment.html', {'event': event, 'tickets': tickets_booked})


@login_required(login_url='home')
def payment_success(request):
    event_id = request.session.get('event_id')
    tickets_booked = request.session.get('tickets_booked')

    if not event_id or not tickets_booked:
        messages.error(request, "Payment information missing.")
        return redirect('event_list')

    event = Event.objects.get(id=event_id)
    tickets_booked = int(tickets_booked)

    if event.total_tickets >= tickets_booked:
        event.total_tickets -= tickets_booked
        event.save()

        Booking.objects.create(
            customer_data=request.user,
            event=event,
            tickets_booked=tickets_booked,
            payment_status=True
        )

        request.session.flush()
        messages.success(request, "Payment Successful and Booking Confirmed! 🎉")
        return render(request, 'Customer/payment_success.html')

    else:
        messages.error(request, "Tickets sold out. Payment cancelled.")
        return redirect('customer_event_list')

@login_required(login_url='home')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'customer/event_details.html', {'event': event})

@login_required(login_url='home')
def my_bookings(request):
    user = request.user
    bookings = Booking.objects.filter(customer_data=user, payment_status=True)

    return render(request, 'customer/my_bookings.html', {'bookings': bookings})

@login_required(login_url='home')
def customer_profile(request):
    user = request.user
    customer = Login.objects.get(id=user.id)
    return render(request, 'customer/customer_profile.html', {'customer': customer})