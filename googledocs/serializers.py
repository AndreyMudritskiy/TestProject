from rest_framework import serializers
from googledocs.models import Row


class RowSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    field1 = serializers.CharField()
    field2 = serializers.CharField()
    field3 = serializers.CharField()
