from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination
from taki.permissions import IsOwnerOrReadOnly
from solutions.models import Solution
from solutions.serializers import SolutionListSerializer, SolutionDetailSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter


class SolutionResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class SolutionFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='contains')
    oj = filters.CharFilter(field_name="oj", lookup_expr='contains')
    pid = filters.CharFilter(field_name="pid", lookup_expr='contains')
    name = filters.CharFilter(field_name='owner__profile__name', lookup_expr='contains')

    class Meta:
        model = Solution
        fields = ['title', 'oj', 'pid', 'name']


class SolutionList(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    # serializer_class = SolutionListSerializer
    pagination_class = SolutionResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = SolutionFilter
    ordering_fields = ('title', 'oj', 'pid', 'name', 'created')

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return SolutionListSerializer
        return SolutionDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)