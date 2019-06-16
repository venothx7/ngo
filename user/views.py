from django.shortcuts import render
from .models import User

# Create your views here.
from django.http import HttpResponse


def index(request):
    # posts = Posts.objects.all()[:10]
    users = User.objects.all

    context = {
        'users':users
    }

    return render(request, 'user/userlist.html', context)