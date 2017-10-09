

class FoodsManager:

    def __init__(self, DbLayer):
        self.DbLayer = DbLayer

    def Get(self, id):
        return self.DbLayer.FoodsRepository().Get(id)

    def Update(self, id, model):
        self.DbLayer.FoodsRepository().Update(model, id)

    def Insert(self, model):
        self.DbLayer.FoodsRepository().Insert(model)