from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=CustomUser
        fields= UserCreationForm.Meta.fields + ('user_image','email','occupation' ,'address','district','state','contact_details','hobbies','private')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'password1': forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'password'
                }),
        }
class CustomUserChangeForm(UserChangeForm):
    class Meta():
        model=CustomUser
        fields= UserChangeForm.Meta.fields