from DAL.Repository.FoodsRepository import FoodsRepository
from DAL.Dataprovider.GoogleSheets.GoogleSheetsDataProvider import GoogleSheetsDataProvider

class DbLayer:

    def __init__(self):
        self._Context = GoogleSheetsDataProvider()
        self._foodsRepository = None

    def FoodsRepository(self):
        if(self._foodsRepository == None):
            _foodsRepository = FoodsRepository(self._Context)

        return _foodsRepository
