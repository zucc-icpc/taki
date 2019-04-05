from rest_framework import serializers
from templates.models import Template


class TemplateListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Template
        fields = ('id', 'title', 'owner', 'created', 'type', 'pdf', 'word', 'intro')


class TemplateDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Template
        fields = ('id', 'title', 'pdf', 'type', 'owner', 'word', 'intro')

