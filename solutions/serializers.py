from rest_framework import serializers
from solutions.models import Solution


class SolutionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Solution
        fields = "__all__"