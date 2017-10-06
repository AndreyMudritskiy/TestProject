from rest_framework import serializers
from googledocs.models import Row


class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ('field1', 'field2', 'field3')
