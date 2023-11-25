from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from . serializers import ListCustomUserSerializer, CustomUserSerializer, CustomTokenObtainPairSerializer, MessageSerializer, \
    UserGroupsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import CustomUser
from core.models import UserGroups, Message


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer


class ListCustomUsersApiView(ListAPIView):
    serializer_class = ListCustomUserSerializer
    queryset = CustomUser.objects.all()


class DetailCustomUserApiView(RetrieveAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    

class ListUserGroupsApiView(ListAPIView):
    serializer_class = UserGroupsSerializer
    queryset = UserGroups.objects.all()
    permission_classes = [IsAuthenticated]


class CreateUserGroupsApiView(CreateAPIView):
    serializer_class = UserGroupsSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserGroups.objects.all()

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(createdBy=request.user)


class DetailUserGroupsApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserGroupsSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserGroups.objects.all()

    def get_object(self):
        return super().get_object()


class ListMessagesApiView(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = UserGroups.objects.all()


class CreateMessageApiView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        request = serializer.context['request']
        serializer.save(sender=request.user)


class DetailMessageApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()

    def get_object(self):
        return super().get_object()
