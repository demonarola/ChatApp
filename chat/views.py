from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
import json

from .models import ChatRoom

@login_required
def index(request):
    return render(request, 'chat/index.html', {})


@login_required
def room(request, room_name):
    user = None
    token = None
    try:
        room = ChatRoom.objects.get(name=room_name)
        room_id = room.id
    except ChatRoom.DoesNotExist:
        room_id = None
    if not request.user.is_anonymous:
        token = Token.objects.get(user=request.user)
        user = request.user
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'room_id': room_id, 'token': token,
        'user': user.id
    })
