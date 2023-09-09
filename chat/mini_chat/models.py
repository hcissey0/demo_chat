from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations1', default=None)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations2', default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversation between {self.user1.username} and {self.user2.username}'

    
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name="chat_rooms")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
class PrivateMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_private_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_private_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} to {self.recipient.username} : {self.content}'


class ChatRoomMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chatroom_messages')
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username} in {self.chatroom.name} : {self.content}'

    