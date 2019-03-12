from rest_framework import serializers
from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = ('title', 'created', 'content', 'owner')