from rest_framework import generics, permissions
from templates.serializers import TemplateListSerializer, TemplateDetailSerializer
from templates.models import Template
from taki.permissions import IsOwnerOrReadOnly


class TemplateList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TemplateListSerializer
        return TemplateDetailSerializer

    def get_queryset(self):
        queryset = Template.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemplateDetailSerializer
    queryset = Template.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
