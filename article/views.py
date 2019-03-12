from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework import permissions
from article.permissions import IsOwnerOrReadOnly


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
