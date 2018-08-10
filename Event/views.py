from django.shortcuts import render
from .models import Event


def post_list_view(request):
	events = Event.published.all()
	return render(request, 'Event/events.html', {'events': events})

