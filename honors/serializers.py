from rest_framework import serializers
from honors.models import Honor


class HonorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honor
        fields = ('id', 'created', 'intro', 'type', 'time')


class HonorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Honor
        fields = ('id', 'created', 'intro', 'type', 'time', 'detail')