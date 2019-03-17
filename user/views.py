from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from user.serializers import UserSerializer, UserRegisterSerializer, ProfileSerializer, ProfileUpdateSerializer
from user.models import Profile
from user.permissions import IsOwnerOrReadOnly

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['username'], serializer.validated_data['password'])
            User.objects.create_user(
                serializer.validated_data['username'],
                serializer.validated_data['password'],
            )
            return Response(serializer.validated_data['username'], status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = ProfileSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PUT', 'PATCH']:
            return ProfileUpdateSerializer
        else:
            return ProfileSerializer

    # def update(self, request, *args, **kwargs):
    #     serializer = ProfileUpdateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





