from rest_framework import permissions, generics
from rest_framework.pagination import PageNumberPagination
from taki.permissions import IsNotGuest, IsCoachOrSelf
from reports.models import Report
from reports.serializers import ReportListSerializer, ReportDetailSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter


class ReportResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ReportFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='contains')
    name = filters.CharFilter(field_name='owner__profile__name', lookup_expr='contains')

    class Meta:
        model = Report
        fields = ['title', 'name']


class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    # serializer_class = SolutionListSerializer
    pagination_class = ReportResultsSetPagination
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = ReportFilter
    ordering_fields = ('title', 'name', 'created')
    permission_classes = (IsNotGuest,)

    def get_queryset(self):
        queryset = Report.objects.all()
        owner = self.request.query_params.get('owner', None)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        return queryset

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ReportListSerializer
        return ReportDetailSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportDetailSerializer
    permission_classes = (IsCoachOrSelf,)
