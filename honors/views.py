from rest_framework import generics
from taki.permissions import IsStaffOrReadOnly
from honors.serializers import HonorListSerializer
from honors.models import Honor


class HonorList(generics.ListCreateAPIView):
    permission_classes = (IsStaffOrReadOnly, )
    serializer_class = HonorListSerializer
    queryset = Honor.objects.all()