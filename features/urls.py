from django.urls import path ,re_path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('user/profile/<int:id>',views.UserProfileView,name='profile'),

    path('friends',views.friends,name='friends'),
    path('friends/delete/<int:id>',views.friendDeleteView,name='deletefriend'),
    path('friends/accept/<int:id>',views.friendApproveView,name='acceptfriend'),
    path('friends/request/<int:id>',views.friendRequestView,name='requestfriend'),
    path('friends/chat/<int:user2id>',views.chat_room,name='chat_room'),

    re_path(r'^search(?:search=(?P<search>)/)?$',views.searchView,name='search'),
]