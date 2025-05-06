from django.urls import path

from event_app import views, EventOwner_views, customer_views, admin_views

urlpatterns = [
    path('',views.home,name="home"),
    #User Authentication&Authorization
    path('customer_add', views.customer_add, name="customer_add"),
    path('EventOwner', views.EventOwner_add, name="EventOwner_add"),
    path('login_views', views.login_views, name='login_views'),
    path('logout_view', views.logout_view, name='logout_view'),
    #dashboards
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('customer_dashboard', views.customer_dashboard, name="customer_dashboard"),
    path('EventOwner_dashboard', views.EventOwner_dashboard, name="EventOwner_dashboard"),
    #event_Owner
    path('event_upload',EventOwner_views.event_upload,name='event_upload'),
    path('event_details',EventOwner_views.event_details,name='event_details'),
    path('update_events/<int:id>/',EventOwner_views.update_events,name='update_events'),
    path('delete_events/<int:id>/',EventOwner_views.delete_events,name='delete_events'),
    path('event_details/', EventOwner_views.event_details, name='event_details'),
    path('payment_tracking/', EventOwner_views.payment_tracking, name='payment_tracking'),
    path('profile/', EventOwner_views.event_owner_profile, name='event_owner_profile'),
    #customer
    path('event_list/', customer_views.event_list, name='event_list'),
    path('book_now/<int:event_id>/', customer_views.book_now, name='book_now'),
    path('payment_page/<int:event_id>/', customer_views.payment_page, name='payment_page'),
    path('payment_success/', customer_views.payment_success, name='payment_success'),
    path('event_details/<int:event_id>/', customer_views.event_details, name='event_details'),
    path('payment/<int:event_id>/', customer_views.card_payment, name='card_payment'),
    path('my_bookings/', customer_views.my_bookings, name='my_bookings'),
    path('profile/',customer_views.customer_profile, name='customer_profile'),

    #admin
    path('customer_details/', admin_views.customer_details, name='customer_details'),
    path('delete_customer/<int:customer_id>/',admin_views.delete_customer,name='delete_customer'),
    path('toggle-customer/<int:customer_id>/', admin_views.toggle_customer_status, name='toggle_customer'),
    path('EventOwner_details/', admin_views.EventOwner_details, name='EventOwner_details'),
    path('delete_EventOwner/<int:EventOwner_id>/',admin_views.delete_EventOwner,name='delete_EventOwner'),
    path('toggle-EventOwner/<int:EventOwner_id>/', admin_views.toggle_EventOwner_status, name='toggle_EventOwner'),
    path('events_list/', admin_views.events_list, name='events_list'),







]