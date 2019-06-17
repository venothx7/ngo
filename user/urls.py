# urls.py
from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDelete

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', UserCreateView.as_view(), name='user-create'),
    path('delete/<int:pk>', UserDelete.as_view(), name='user-delete'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user-update'),

]
