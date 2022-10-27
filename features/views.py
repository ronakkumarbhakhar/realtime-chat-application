from multiprocessing import context
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, TemplateView
from . import models
# Create your views here.

# functions to be used in views ------------------------------------------------------------------------->

def find_friends(user):
    current_user=get_user_model().objects.get(pk=user.pk)
    frnd_sent_accepted=current_user.frnd_rqst_sent.filter(accepted=True)
    frnd_received_accepted=current_user.frnd_rqst_received.filter(accepted=True)
    frnd_sent_not_accepted=current_user.frnd_rqst_sent.filter(accepted=False)
    frnd_received_not_accepted=current_user.frnd_rqst_received.filter(accepted=False)

    friends={'sent_accepted':frnd_sent_accepted,
             'received_accepted':frnd_received_accepted,
             'sent_not_accepted':frnd_sent_not_accepted,
             'received_not_accepted':frnd_received_not_accepted
            }
    return friends


# views -------------------------------------------------------------------------------------------------->

class IndexView(TemplateView):
    template_name='index.html'

#------------------------------------------------friendsview------------------------------------->
def friends(request):

    user=request.user
    current_user=get_user_model().objects.get(pk=user.pk)
    frnd_sent_accepted=current_user.frnd_rqst_sent.filter(accepted=True)
    frnd_received_accepted=current_user.frnd_rqst_received.filter(accepted=True)
    frnd_sent_not_accepted=current_user.frnd_rqst_sent.filter(accepted=False)
    frnd_received_not_accepted=current_user.frnd_rqst_received.filter(accepted=False)

    def number_of_items(model):
        length= len(model)
        return int(length)

    friends={
             'sent_accepted':frnd_sent_accepted,
             'accepted_no':number_of_items(frnd_sent_accepted)+number_of_items(frnd_received_accepted),
             'received_accepted':frnd_received_accepted,
             'sent_not_accepted':frnd_sent_not_accepted,
             'sent_not_accepted_no':number_of_items(frnd_sent_not_accepted),
             'received_not_accepted':frnd_received_not_accepted,
             'received_not_accepted_no':number_of_items(frnd_received_not_accepted),
            }
    return render(request, 'features/friends.html', {'friends':friends})


# --------------------------------------------------friendDeleteview----------------------------------------->
def friendDeleteView(request,id):
    entry=models.Friend.objects.get(id=id)
    entry.delete()
    res = {
        'deleted':True
    }
    
    print(res)
    return JsonResponse(res)

# -----------------------------------------------friendApproveView---------------------------------------->

def friendApproveView(request,id):
    entry=models.Friend.objects.get(id=id)
    entry.approved()
    res = {
        'approved':True
    }
    
    print(res)
    return JsonResponse(res)
    

#------------------------------------------------------------searchView-----------------------------------> 

def searchView(request):
    searchquery=request.GET.get('search',"")
    current_user=get_user_model().objects.get(pk=request.user.pk)

    reslutlist=get_user_model().objects.filter(username__icontains=searchquery) | get_user_model().objects.filter(first_name__icontains=searchquery)
    
    frnd_sent_accepted=[]
    frnd_received_accepted=[]
    frnd_sent_not_accepted=[]
    frnd_received_not_accepted=[]
    not_friend=[]

    # this function does not tell difference between requested user or approved friend so don't use as universal friend finder
    def friends_or_not(user1,user2):
        frnd_sent_user1=user1.frnd_rqst_sent.filter(sent_to=user2)
        frnd_sent_user2=user2.frnd_rqst_sent.filter(sent_to=user1)

        frndlist1_len=len(frnd_sent_user1)
        frndlist2_len=len(frnd_sent_user2)
        
        if(frndlist1_len>0 or frndlist2_len>0):
            return True
        
        return False
        
    def number_of_items(model):
        length= len(model)
        return int(length)

    for resultuser in reslutlist:
        if friends_or_not(current_user,resultuser):
            frnd_sent_accepted.extend(current_user.frnd_rqst_sent.filter(accepted=True).filter(sent_to=resultuser))
            frnd_received_accepted.extend(current_user.frnd_rqst_received.filter(accepted=True).filter(sent_by=resultuser))
            frnd_sent_not_accepted.extend(current_user.frnd_rqst_sent.filter(accepted=False).filter(sent_to=resultuser))
            frnd_received_not_accepted.extend(current_user.frnd_rqst_received.filter(accepted=False).filter(sent_by=resultuser))
        else:
            if(resultuser != request.user):
                not_friend.append(resultuser)

    results={'sent_accepted':frnd_sent_accepted,
             'accepted_no':number_of_items(frnd_sent_accepted)+number_of_items(frnd_received_accepted),
             'received_accepted':frnd_received_accepted,
             'sent_not_accepted':frnd_sent_not_accepted,
             'sent_not_accepted_no':number_of_items(frnd_sent_not_accepted),
             'received_not_accepted':frnd_received_not_accepted,
             'received_not_accepted_no':number_of_items(frnd_received_not_accepted),
             "not_friend":not_friend,
             "not_friend_no":number_of_items(not_friend),
             "total":number_of_items(frnd_sent_accepted)+number_of_items(frnd_received_accepted)+number_of_items(not_friend)+number_of_items(frnd_sent_not_accepted)+number_of_items(frnd_received_not_accepted),
            }
    
    return render(request, 'features/search.html', {'results':results})


def chat_room(request,user2id):
    user1=request.user
    # user2=get_user_model().objects.get(id=user2id)

    if user1.id<=user2id:
        user1_id=str(user1.id)
        user2_id=str(user2id)
        room_name=user1_id+'--'+user2_id
    else:
        user1_id=str(user1.id)
        user2_id=str(user2id)
        room_name=user2_id+'--'+user1_id

    chats=models.Chat.objects.filter(roomname=room_name).order_by('date')

    context={'user1':user1.id,
             'user2':user2id,
             'room_name':room_name,
             'chats':chats,
            }

    
    return render(request, 'features/chat_room.html', {'context':context})


def UserProfileView(request,id):
    user=get_user_model().objects.get(id=id)

    def exact_friends_or_not(user1,user2):
        frnd_sent_user1=user1.frnd_rqst_sent.filter(sent_to=user2)
        frnd_sent_user2=user2.frnd_rqst_sent.filter(sent_to=user1)

        frndlist1_len=len(frnd_sent_user1)
        frndlist2_len=len(frnd_sent_user2)
        bool=False
        if(frndlist1_len>0 ):
            if(frnd_sent_user1[0].accepted):
                bool=True
        if(frndlist2_len>0):
            if(frnd_sent_user2[0].accepted):
                bool=True
        
        return bool

    friend=exact_friends_or_not(request.user,user)
    context={'user':user,'friend':friend}
    return render(request,'features/profile.html',{'context':context})

def SettingView(request):
    return render(request,'features/setting.html')

def friendRequestView(request,id):
    friend=get_user_model().objects.get(id=id)
    frnd_rqst=models.Friend(sent_by=request.user,sent_to=friend)
    frnd_rqst.save()
    res = {
        'created':True
    }
    
    print(frnd_rqst)
    return JsonResponse(res)