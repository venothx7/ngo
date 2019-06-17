from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect


from .models import User
from .forms import UserForm


class UserCreateView(CreateView):
    template_name = 'user/user_create.html'
    success_url = '/user'
    form_class = UserForm

    # this part shows the entered info in console
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    template_name = 'user/user_create.html'
    queryset = User.objects.all()
    success_url = '/user'
    form_class = UserForm


class UserDelete(DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = ('/user')


def index(request):
    # posts = Posts.objects.all()[:10]
    users = User.objects.all
    context = {
        'users': users
    }
    return render(request, 'user/userlist.html', context)
