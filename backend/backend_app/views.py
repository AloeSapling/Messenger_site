from rest_framework.response import Response
from rest_framework import status
from backend_app.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import authenticate, get_user_model
from rest_framework.viewsets import GenericViewSet
from backend_app.serializers import UserSerializer, BlacklistSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from backend_app.permissions import IsNotBlacklisted
from backend_app.models import AccessTokenBlacklist
User = get_user_model()
class UserViewSet(GenericViewSet):
    serializer_class = UserSerializer
    
    @permission_classes([IsAuthenticated])
    @action(detail=False, methods=['get'])
    def get_current(self,request):
        user_id = request.user.id
        return Response({"user_id": user_id}, status=status.HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def login(self, request):
        form = CustomAuthenticationForm(data=request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
        return Response({'error': form.errors}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=False, methods=['post'])
    def register(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return Response(form.data,status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['put'])
    def logout(self,request):
        return Response(status=status.HTTP_200_OK)
class TokenViewSet(GenericViewSet):
    @action(detail=False, methods=['post'])
    @permission_classes([IsAuthenticated])
    def refresh(self,request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)
            refresh = RefreshToken(refresh_token)
            refresh.blacklist()

            old_access_token = request.headers.get('Authorization')
            blacklist_instance= BlacklistSerializer(data={"token": str(old_access_token)})
            blacklist_instance.is_valid(raise_exception=True)
            blacklist_instance.save()

            new_access_token = refresh.access_token
            new_refresh_token = RefreshToken.for_user(User.objects.get(id=refresh.payload['user_id']))
            response_data = {
                "access_token": str(new_access_token),
                "refresh_token": str(new_refresh_token),
                "blacklisted_access_token": str(old_access_token),
                "blacklisted_refresh_token": str(refresh)
            }
            return Response(response_data)
        except InvalidToken:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({'error': 'Blacklisted token'}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False,methods=['get'])
    def get_blacklist(self,request):
        blacklist = BlacklistSerializer(AccessTokenBlacklist.objects.all(), many=True)
        return Response(blacklist.data)