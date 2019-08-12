from rest_framework import serializers
from solutions.models import Solution


class SolutionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    name = serializers.ReadOnlyField(source="owner.profile.name")

    class Meta:
        model = Solution
        fields = ('id', 'created', 'title', 'oj', 'pid', 'owner', 'content', 'name')


class SolutionListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    name = serializers.ReadOnlyField(source="owner.profile.name")
    created = serializers.DateTimeField(format="%Y年%m月%d日 %H:%M", required=False, read_only=True)

    class Meta:
        model = Solution
        fields = ('id', 'created', 'title', 'oj', 'pid', 'owner', 'name')
