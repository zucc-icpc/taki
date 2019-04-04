import os

from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from user.serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer, ProfileUpdateSerializer, ProfileAvatarSerializer
from user.models import Profile
from user.serializers import UserSerializer
from user.permissions import IsOwnerOrReadOnly
from taki import settings
from django.core.files import uploadhandler
from django.core.files.storage import default_storage
from user.permissions import CreateOnly


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


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

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


# class FileUploadView(APIView):
#     parser_classes = (MultiPartParser, )
#
#     def post(self, request):
#         serializer = ProfileAvatarSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(
#                 data=serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
