from django.contrib.auth.models import User
from rest_framework import serializers
from mini_chat.models import Conversation, PrivateMessage, ChatRoom, ChatRoomMessage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class ConversationSerializer(serializers.ModelSerializer):
    user1 = UserSerializer()
    user2 = UserSerializer()
    
    class Meta:
        model = Conversation
        fields = '__all__'  


class PrivateMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    recipent = UserSerializer()
    
    class Meta:
        model = PrivateMessage
        fields = '__all__'       
        
        
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        
        
class ChatRoomMessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    
    class Meta:
        model = ChatRoomMessage
        fields = '__all__'