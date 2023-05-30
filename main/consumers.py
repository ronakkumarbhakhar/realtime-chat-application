import json
from channels.db import database_sync_to_async
from channels.generic.websocket import  AsyncWebsocketConsumer
from features.models import Chat
from django.contrib.auth import get_user_model


class ChatConsumer( AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = str(self.scope["url_route"]["kwargs"]["room_name"])
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        print(close_code)
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = text_data_json["sender"]
        receiver = text_data_json["receiver"]
        roomname = text_data_json["roomname"]

        await self.set_chat(sender=sender,message=message,receiver=receiver,roomname=roomname)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message,"sender":sender,"receiver":receiver,"roomname":roomname}
        )   

        

    @database_sync_to_async
    def set_chat(self,sender,message,receiver,roomname):
        sender_user=get_user_model().objects.get(id=sender)
        receiver_user=get_user_model().objects.get(id=receiver)
        chat=Chat(sent_by=sender_user,sent_to=receiver_user,chat=message,roomname=roomname)
        chat.save()
        
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]
        receiver = event["receiver"]
        roomname = event["roomname"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message,"sender":sender,"receiver":receiver,"roomname":roomname}))