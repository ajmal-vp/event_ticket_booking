import django_filters
from django_filters import ChoiceFilter, CharFilter
from .models import Event
from django import forms


class CategoryFilter(django_filters.FilterSet):
    category = ChoiceFilter(
        choices=Event.CATEGORY_CHOICES,
        label="",
        widget=forms.Select(attrs={'class': 'form-select'}),
    )

    class Meta:
        model = Event
        fields = ['category']

class EventFilter(django_filters.FilterSet):
    event_name = django_filters.CharFilter(
        label="",
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Search Event Name', 'class': 'form-control'})
    )
    category = django_filters.ChoiceFilter(
        choices=Event.CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Event
        fields = ['category', 'event_name']