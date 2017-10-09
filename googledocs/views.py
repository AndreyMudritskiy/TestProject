# Create your views here.

from googledocs.serializers import FoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DAL.DbLayer import DbLayer
from googledocs.FoodsManager import FoodsManager


class BaseViews(APIView):
    dbLayer = DbLayer()


class Foods(BaseViews):

    def __init__(self):
        self._foodsManager = FoodsManager(self.dbLayer)

    def get(self, request, id):
        Food = self._foodsManager.Get(id)
        if Food is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FoodSerializer(Food)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            self._foodsManager.Update(id, serializer.RestoreModel())
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            self._foodsManager.Insert(serializer.RestoreModel())
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
