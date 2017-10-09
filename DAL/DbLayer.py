from DAL.IDbLayer import IDbLayer
from DAL.Repository.FoodsRepository import FoodsRepository

class DbLayer(IDbLayer):

    def __init__(self):
        self._foodsRepository = None

    def FoodsRepository(self):
        if self._foodsRepository is None:
            self._foodsRepository = FoodsRepository()

        return self._foodsRepository
