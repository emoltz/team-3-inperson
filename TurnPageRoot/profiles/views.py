from django.shortcuts import render
from django.views.generic import *
from .models import *


# Create your views here.
class LoginView(TemplateView):
    template_name = 'profiles/login.html'
    extra_context = {}


class SignupView(TemplateView):
    template_name = 'profiles/signup.html'
    extra_context = {}
