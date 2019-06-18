from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import Profile
from easy_thumbnails.templatetags.thumbnail import thumbnail_url
from easy_thumbnails.files import get_thumbnailer
from django.http import HttpRequest


class ThumbnailSerializer(serializers.ImageField):
    def to_representation(self, instance):
        if instance == '':
            return None
        return get_thumbnailer(instance)['avatar'].url


class UserSerializer(serializers.ModelSerializer):
    # profile = serializers.PrimaryKeyRelatedField(read_only=True)
    type = serializers.CharField(source='profile.type')
    biography = serializers.CharField(source='profile.biography')
    avatar = serializers.ImageField(source='profile.avatar')
    name = serializers.CharField(source='profile.name')
    sid = serializers.CharField(source='profile.sid')
    avatar_thumb = ThumbnailSerializer(source='profile.avatar')

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'type', 'biography', 'avatar', 'name', 'sid', 'email', 'avatar_thumb')


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username')
    avatar_thumb = ThumbnailSerializer(source='avatar')
    is_staff = serializers.CharField(source='user.is_staff')

    class Meta:
        model = Profile
        fields = (
            'user', 'username', 'created_at', 'updated_at', 'type', 'is_staff',
            'biography', 'avatar', 'name', 'sid', 'level', 'work', 'graduate', 'avatar_thumb'
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    avatar_thumb = ThumbnailSerializer(source='avatar')

    class Meta:
        model = Profile
        fields = (
            'type', 'biography', 'avatar', 'name', 'sid', 'level', 'work', 'graduate', 'avatar_thumb'
        )

    def validate_type(self, value):
        if value not in ['普通用户', '队员', '教练', '退役队员']:
            raise serializers.ValidationError("用户类型不正确")
        return value


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'avatar'
        )