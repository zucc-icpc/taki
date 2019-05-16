from rest_framework import serializers
from solutions.models import Solution


class SolutionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Solution
        fields = ('id', 'created', 'title', 'oj', 'pid', 'owner', 'content')


class SolutionListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    created = serializers.DateTimeField(format="%Y年%m月%d日 %H:%M", required=False, read_only=True)

    class Meta:
        model = Solution
        fields = ('id', 'created', 'title', 'oj', 'pid', 'owner')