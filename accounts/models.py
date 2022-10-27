from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # Ocupations =[
    #                 ('CO', 'Company'),
    #                 ('SU', 'Student'),
    #                 ('CJ', 'Teacher'),
    #                 ('UN','Ohter'),
    #             ]
    occupation = models.CharField(max_length=200,default='unknown',blank=True,null=True)


    address= models.CharField(max_length=500,null=True,blank=True)
    district= models.CharField(max_length=100,null=True,blank=True)
    state=  models.CharField(max_length=100,null=True,blank=True)
    contact_details= models.PositiveIntegerField(null=True,blank=True)
    user_image=models.ImageField(default=None,blank=True,null=True)
    hobbies=models.TextField(default='No Hobbies',null=True,blank=True)
    private=models.BooleanField(default=True)

    def make_public(self):
         self.private=False
         self.save()

    def make_private(self):
        self.private=True
        self.save()