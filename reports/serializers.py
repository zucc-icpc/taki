from rest_framework import serializers
from reports.models import Report


class ReportDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    name = serializers.ReadOnlyField(source="owner.profile.name")
    created = serializers.DateTimeField(format="%Y年%m月%d日 %H:%M", required=False, read_only=True)

    class Meta:
        model = Report
        fields = ('id', 'created', 'title', 'owner', 'content', 'name')


class ReportListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    name = serializers.ReadOnlyField(source="owner.profile.name")
    created = serializers.DateTimeField(format="%Y年%m月%d日 %H:%M", required=False, read_only=True)

    class Meta:
        model = Report
        fields = ('id', 'created', 'title', 'owner', 'name')
