# Create your views here.

from googledocs.models import Row
from googledocs.serializers import RowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Rows(APIView):

    def get(self, request,id):
        row = Row()
        row.field1 = 'hello'
        row.field2 = 'world'
        row.field3 = 'id='+id
        serializer = RowSerializer(row)
        return Response(serializer.data)
