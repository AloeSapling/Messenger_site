from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from backend_app.serializers import MessageSerializer, CustomUserSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from backend_app.models import Message, CustomUser
# Create your views here.
class MessageViewSet(GenericViewSet):
    serializer_class = MessageSerializer

    @action(detail=False, methods=['get']
    # , permission_classes=[IsAuthenticated]
    )
    def get_all(self, request):
        messages = Message.objects.all()
        messages = self.serializer_class(messages, many=True)
        return Response(messages.data)
    @action(detail=False, methods=["post"])
    def message(self, request):
        message = self.serializer_class(data=request.data)
        message.is_valid(raise_exception=True)
        message.save()
        return Response("Message sent.")
class UserViewSet(GenericViewSet):
    serializer_class = CustomUserSerializer
    
    @action(detail=False, methods=['post'])
    def register(self, request):
        user = CustomUser.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
        user.name = request.POST.get('name')
        return Response(request.POST.get('username'))