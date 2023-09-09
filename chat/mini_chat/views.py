from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from mini_chat.models import ChatRoom, ChatRoomMessage, Conversation, PrivateMessage
from mini_chat.serializers import UserSerializer, ChatRoomSerializer, ChatRoomMessageSerializer, ConversationSerializer, PrivateMessageSerializer


# Create your views here.

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class ConversationList(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    
    
class PrivateMessageList(viewsets.ModelViewSet):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    
    
class ChatRoomList(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
    
class ChatRoomMessageList(viewsets.ModelViewSet):
    queryset = ChatRoomMessage.objects.all()
    serializer_class = ChatRoomMessageSerializer


def index(request):
    return render(request, 'index.html')

