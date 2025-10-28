from rest_framework import serializers


class PortfolioDataSerializer(serializers.Serializer):
    """Serializer pour les données du portfolio"""
    name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    current_work = serializers.CharField()
    projects = serializers.ListField(
        child=serializers.DictField()
    )
    contact = serializers.DictField()
    tools = serializers.ListField(
        child=serializers.DictField()
    )
