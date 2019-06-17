import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.contrib.auth.models import User
from user.serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer, ProfileUpdateSerializer, ProfileAvatarSerializer
from user.models import Profile
from user.serializers import UserSerializer
from user.permissions import IsOwnerOrReadOnly
from easy_thumbnails.files import get_thumbnailer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST']:
            return UserRegisterSerializer
        else:
            return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email']
            )
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_200_OK)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Profile.objects.all()
        type = self.request.query_params.get('type', None)
        if type is not None:
            queryset = queryset.filter(type=type)
        return queryset


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # def perform_update(self, serializer):
    #     instance = self.get_object()
    #     avatar = instance.avatar
    #     serializer.save(avatar_thumb=get_thumbnailer(avatar)['avatar'].url)

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            return ProfileUpdateSerializer
        else:
            return ProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    # def update(self, request, *args, **kwargs):
    #     serializer = ProfileUpdateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def verify_user(request):
    data = {
        "id": request.user.id,
        "isLogin": "true"
    }
    if request.user.is_anonymous:
        data = {
            "isLogin": "false"
        }
    return Response(data=data, status=status.HTTP_200_OK)
