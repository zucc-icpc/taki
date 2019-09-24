from rest_framework import permissions, generics
from taki.permissions import IsStaffOrReadOnly
from honors.serializers import HonorListSerializer, HonorDetailSerializer
from honors.models import Honor


class HonorList(generics.ListCreateAPIView):
    permission_classes = (IsStaffOrReadOnly, )
    queryset = Honor.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return HonorListSerializer
        return HonorDetailSerializer


class HonorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsStaffOrReadOnly, )
    serializer_class = HonorDetailSerializer
    queryset = Honor.objects.all()
