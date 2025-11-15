from django.shortcuts import render
from .models import Event, BirthDayEvent


def home(request):
    events = Event.objects.all()
    birthdays = BirthDayEvent.objects.all()
    
    return render(request, 'main/home.html', context={
        'events': events,
        'birthdays': birthdays
        }
    )
