from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.views import generic
from .models import User
from .forms import UserForm

class Index(generic.ListView):
    model = User
    context_object_name = 'users'
    template_name = 'user/userlist.html'

class UserCreateView(BSModalCreateView):
    template_name = 'user/user_create.html'
    success_url = '/user'
    form_class = UserForm
    success_message = 'Success: Book was created.'


class UserUpdateView(BSModalUpdateView):
    template_name = 'user/user_create.html'
    queryset = User.objects.all()
    success_url = '/user'
    success_message = 'Success: Book was updated.'
    form_class = UserForm


class UserDelete(BSModalDeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = ('/user')
    success_message = 'Success: Book was deleted.'



