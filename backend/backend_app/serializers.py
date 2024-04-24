from backend_app.models import Message, CustomUser
from rest_framework.serializers import ModelSerializer
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields ="__all__"
class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields ="__all__"