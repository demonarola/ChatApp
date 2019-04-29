# -*- coding: utf-8 -*-

from rest_framework import routers

from chat.viewsets import ChatMessageViewSet
app_name = 'chat_api'

router = routers.DefaultRouter()
router.register(r'messages', ChatMessageViewSet, base_name='chatmessages')
