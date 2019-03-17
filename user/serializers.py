from rest_framework import serializers
from django.contrib.auth.models import User
from article.models import Article
from user.models import Profile


class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'articles', 'profile')


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = (
            'id', 'username', 'created_at', 'updated_at', 'type',
            'biography', 'avatar', 'name', 'sid'
        )
