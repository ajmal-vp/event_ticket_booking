from django import forms
from django.contrib.auth.forms import UserCreationForm

from event_app.models import Login, Customer, EventOwner, Event, Booking


class login_Form(UserCreationForm):

    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ("username","password1","password2",'email')

class Customer_login(forms.ModelForm):


    class Meta:
        model = Customer
        fields = ("phone_no","name")

class EventOwner_login(forms.ModelForm):

    class Meta:
        model = EventOwner
        fields = ("phone_no","Gst_no","event_category")

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image','event_name', 'description', 'event_date', 'venue', 'total_tickets', 'price_per_ticket','category','about_event']
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tickets_booked']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['tickets_booked'].widget.attrs.update({'class': 'form-control', 'min': 1})