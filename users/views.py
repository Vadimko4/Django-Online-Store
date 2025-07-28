import secrets

from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

# from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User



class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url =  reverse_lazy('users:login')
