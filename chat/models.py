from django.db import models
from django.conf import settings

from accounts.models import User


class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatMessages(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="message_user")
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, related_name="message_room")
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)