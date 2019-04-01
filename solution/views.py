from rest_framework import permissions
from rest_framework import generics
from taki.permissions import IsOwnerOrReadOnly
from solution.models import Solution
from solution.serializers import SolutionSerializer


class SolutionList(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)