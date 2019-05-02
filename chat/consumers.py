# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import ChatRoom, ChatMessages
from accounts.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        room, created = ChatRoom.objects.get_or_create(name=self.room_name)
        room.user.add(User.objects.get(username=self.scope["user"]))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        room, created = ChatRoom.objects.get_or_create(name=self.room_name)
        message_object = ChatMessages.objects.create(message=message, user=User.objects.get(username=self.scope["user"]),
                                    chat_room=room)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'id': message_object.id,
                'created_at': str(message_object.created_at),
                'user': message_object.user_id,
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'id': event['id'],
            'created_at': event['created_at'],
            'user': event['user']
        }))
