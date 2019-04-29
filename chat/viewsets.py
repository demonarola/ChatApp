
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from .models import ChatMessages
from .serializers import ChatMessageSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Chat messages.
    """
    queryset = ChatMessages.objects.all()
    serializer_class = ChatMessageSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('chat_room',)
    search_fields = ('message',)

