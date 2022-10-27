from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class CustomSignupView(CreateView):
    template_name='registration/signup.html'
    form_class= CustomUserCreationForm
    success_url= reverse_lazy('login')