from rest_framework.permissions import BasePermission
from backend_app.models import AccessTokenBlacklist
class IsNotBlacklisted(BasePermission):
    print("IsnotBlacklisted?")
    def has_permission(self, request, view):
        # token = request.headers.get('Authorization')
        # if token is None:
        #     return False
        # if AccessTokenBlacklist.objects.filter(token=token).exists():
        #     return False
        print("IsnotBlacklisted?")
        return False