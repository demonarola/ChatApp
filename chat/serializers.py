from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend

from .models import ChatMessages


class ChatMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessages
        fields = ('id', 'message', 'user', 'chat_room', 'created_at')
