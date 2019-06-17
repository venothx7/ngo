from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

from .models import Event
# from .forms import EventFrom

# Create your views here.



def index(request):
    # posts = Posts.objects.all()[:10]
    events = Event.objects.all
    context = {
        'events': events
    }
    return render(request, 'event/event_list.html', context)