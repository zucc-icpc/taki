from rest_framework import serializers
from honors.models import Honor


class HonorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Honor
        fields = "__all__"
