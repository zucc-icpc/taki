from rest_framework import serializers
from django.contrib.auth.models import User
from article.models import Article

class UserSerializer(serializers.ModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'articles')