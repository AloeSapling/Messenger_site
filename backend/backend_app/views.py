from django.shortcuts import render
from .serializers import MessagesSerializer, UserSerializer, ChatsSerializer
from rest_framework.response import Response
from .models import Messages, User, Chats
from rest_framework import viewsets, status
from django.contrib.auth import authenticate, login
from rest_framework.decorators import action
# Create your views here.
class MessageViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def get_messages(self,request):
        messages = Messages.objects.all()
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['post'])
    def message(self, request):
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UsersViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            password = serializer.validated_data.get('password')
            user = User.objects.create_user(name=name, password=password)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('name')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    @action(detail=True, methods=['get'])
    def get_user(self,request,pk):
        users = User.objects.get(id=pk)
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data)
    @action(detail=False, methods=['gets'])
    def get_self(self,request):
        return Response(request.user)