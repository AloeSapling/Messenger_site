from rest_framework.serializers import ModelSerializer
from backend_app.models import CustomUser, AccessTokenBlacklist
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'
class BlacklistSerializer(ModelSerializer):
    class Meta:
        model = AccessTokenBlacklist
        fields = ['token']