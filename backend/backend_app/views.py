from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from backend_app.serializers import MessageSerializer, CustomUserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from backend_app.models import Message, CustomUser, Chat
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class MessageViewSet(GenericViewSet):
    serializer_class = MessageSerializer

    @action(detail=False, methods=['get']
    , permission_classes=[IsAuthenticated]
    )
    def get_all(self, request):
        messages = Message.objects.all()
        messages = self.serializer_class(messages, many=True)
        return Response(messages.data)
    @action(detail=False, methods=["put"])
    def delete_all(self,request):
        messages = Message.objects.all()
        messages.delete()
        return Response(status=status.HTTP_200_OK)
    @action(detail=False, methods=["post"])
    def message(self, request):
        message = self.serializer_class(data=request.data)
        message.is_valid(raise_exception=True)
        message.save()
        return Response({"message":"Message sent.","content":request.data['content']})
class UserViewSet(GenericViewSet):
    serializer_class = CustomUserSerializer
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        user = CustomUser.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        user.name = request.POST.get('name')
        return Response(request.POST.get('username'))
    @action(detail=False, methods=['POST'])
    @csrf_exempt
    def login(self,request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            sessionid = request.session.session_key
            return Response({'message': "Logged in!", 'sessionid': sessionid})
        else:
            return Response({'message': "Invalid credentials provided",'username': username, 'password': password}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['PUT','POST'])
    def logout(self, request):
        user = request.user
        if user.is_authenticated:
            return Response({"username": user.username}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No user is currently logged in!"}, status=status.HTTP_400_BAD_REQUEST)
class ChatViewSet(GenericViewSet):
    @action(detail=True, methods=['PUT', 'POST'], permission_classes=[IsAuthenticated])
    def join_self(self, request, pk):
        user = request.user
        chat = Chat.objects.get_or_create(id=pk)
        if chat[0].users.filter(id=user.id).exists():
            return Response("You are already in this chat", status=status.HTTP_403_FORBIDDEN)
        else:
            chat[0].users.add(user)
    