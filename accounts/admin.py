from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm,CustomUserCreationForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display=['id','username','user_image','email','occupation','is_staff','address','district','state','contact_details','hobbies','private',]
    fieldsets= UserAdmin.fieldsets + ((None,{'fields':('user_image','occupation','address','district','state','contact_details','hobbies','private',)}),)
    add_fieldsets= UserAdmin.add_fieldsets + ((None,{'fields':('user_image','occupation','address','district','state','contact_details','hobbies','private',)}),)

admin.site.register(CustomUser,CustomUserAdmin)