# Create your views here.

from googledocs.models import Row
from googledocs.serializers import RowSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseViews(APIView):
    field = "(APIView)"


class Rows(BaseViews):

    def get(self, request,id):
        row = Row()
        row.field1 = 'hello' + self.field
        row.field2 = 'world'
        row.field3 = 'id='+id
        serializer = RowSerializer(row)
        return Response(serializer.data)

    def post(self, request):
        serializer = RowSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = RowSerializer(data=request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
