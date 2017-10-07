from DAL.Repository.FoodsRepository import FoodsRepository
from DAL.Dataprovider.GoogleSheets.GoogleSheetsDataProvider import GoogleSheetsDataProvider

class DbLayer:

    def __init__(self, context):
        self._Context = context
        self._foodsRepository = None

    def FoodsRepository(self):
        if self._foodsRepository is None:
            self._foodsRepository = FoodsRepository(self._Context)

        return self._foodsRepository
