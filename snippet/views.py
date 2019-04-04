from rest_framework import permissions, generics
from snippet.models import Snippet
from snippet.serializers import SnippetSerializer
from snippet.permission import IsCodebaseOwnerOrReadOnly
from codebase.models import Codebase


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsCodebaseOwnerOrReadOnly)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsCodebaseOwnerOrReadOnly)

    def perform_create(self, serializer):
        codebase = Codebase.objects.get(id=self.request.data['codebase'])
        serializer.save(owner=self.request.user, codebase=codebase)
