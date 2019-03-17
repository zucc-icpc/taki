from rest_framework import viewsets
from article.models import Article
from user.serializers import UserSerializer
from rest_framework import permissions
from article.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from user.models import Profile
from user.serializers import ProfileSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
