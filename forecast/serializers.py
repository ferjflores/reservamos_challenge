from rest_framework import serializers


class ForecastSerializer(serializers.Serializer):
    city = serializers.CharField()
    country = serializers.CharField()
    forecast = serializers.ListField(child=serializers.DictField())