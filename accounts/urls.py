from django.contrib import admin
from django.urls import path,include
from .views import CustomSignupView
urlpatterns = [
    path('signup/',CustomSignupView.as_view(),name='signup'),
    path('',include('django.contrib.auth.urls')),
]
