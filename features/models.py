from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model

userModel=get_user_model()

# Create your models here.
class Friend(models.Model):
    sent_by=models.ForeignKey(userModel,on_delete=models.CASCADE,related_name='frnd_rqst_sent')
    sent_to=models.ForeignKey(userModel,on_delete=models.CASCADE,related_name='frnd_rqst_received')
    accepted=models.BooleanField(default=False)
    
    def __str__(self):
        sent_by_username=userModel.objects.get(pk=self.sent_by.pk).username
        sent__to_username=userModel.objects.get(pk=self.sent_to.pk).username
        return sent_by_username + "-->" + sent__to_username

    def approved(self):
        self.accepted=True
        self.save()

class Chat(models.Model):
    sent_by=models.ForeignKey(userModel,on_delete=models.CASCADE,related_name='chat_sent')
    sent_to=models.ForeignKey(userModel,on_delete=models.CASCADE,related_name='chat_received')
    chat=models.TextField()
    seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True ,blank=True,null=True)
    roomname=models.CharField(max_length=300,blank=True,null=True)
    
    def __str__(self):
        sent_by_username=userModel.objects.get(pk=self.sent_by.pk).username
        sent__to_username=userModel.objects.get(pk=self.sent_to.pk).username
        return "(" + str(self.id)+ ")" + sent_by_username + "-->" + sent__to_username

    def seen_function(self):
        self.seen=True
        self.save()

class Post(models.Model):
    typeInfo =[
                    ('img', 'image'),
                    ('txt', 'text'),
                ]
    created_by=models.ForeignKey(userModel, on_delete=models.CASCADE,related_name='posts')
    type_of_post=models.CharField(choices=typeInfo ,max_length=50)
    image=models.ImageField(default=None,blank=True,null=True)
    text=models.TextField(default=None,blank=True,null=True)
    caption=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "(" + str(self.id)+ ")" +self.caption