from rest_framework import serializers
from .models import Messages, User, Chats

class MessagesSerializer( serializers.ModelSerializer):
    class Meta:
        model=Messages
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'
class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chats
        fields= '__all__'