from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_EventOwner = models.BooleanField(default=False)

class Customer(models.Model):
    customer_data = models.ForeignKey("Login",on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class EventOwner(models.Model):
    event_owner_data = models.ForeignKey('Login',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=12)
    Gst_no = models.CharField(max_length=10)
    event_category = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class Event(models.Model):
    CATEGORY_CHOICES = [
        ('CONFERENCE', 'Conference'),
        ('WORKSHOP', 'Workshop'),
        ('SEMINAR', 'Seminar'),
        ('MEETUP', 'Meetup'),
        ('WEBINAR', 'Webinar'),
        ('FESTIVAL', 'Festival'),
        ('CONCERT', 'Concert'),
        ('EXHIBITION', 'Exhibition'),
    ]
    event_owner = models.ForeignKey('EventOwner', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    event_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    about_event = models.TextField(blank=True, null=True)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    total_tickets = models.IntegerField()
    price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2)

class Booking(models.Model):
    customer_data = models.ForeignKey("Login",on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets_booked = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)


