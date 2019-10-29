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
        if request.data['name'] is None or request.data['name'].strip() == "":
            return Response({"error": {"真实姓名": ["不能为空"]}}, status=status.HTTP_400_BAD_REQUEST)
        name = request.data['name'].strip()
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email']
            )
            profile = Profile.objects.get(pk=user.id)
            profile.name = name
            profile.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        # host = request.META['HTTP_HOST']
        # for item in data:
        #     if item['avatar_thumb'] is not None:
        #         item['avatar_thumb'] = 'http://' + host + item['avatar_thumb']
        return Response(data)


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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # host = request.META['HTTP_HOST']
        data = serializer.data
        # if data['avatar_thumb'] is not None:
        #     data['avatar_thumb'] = 'http://' + host + data['avatar_thumb']
        return Response(data)


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
