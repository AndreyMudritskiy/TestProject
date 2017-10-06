from DAL.Repository.IRepository import IRepository
from DAL.DomainModel.Food import Food

class FoodsRepository(IRepository):

    def __init__(self,context):
        self.__context = context


    def Get(self, ID):
        listobj = self.__context.GetRow(ID)

        model = Food()
        model.Name = listobj[0]
        model.Proteins = listobj[1]
        model.Fats = listobj[2]

        if(model.IsEmpty()): return None

        return model


    def Insert(self, model):
        repModel = self.GetModelRepresentation(model)
        return self.__context.InsertRow(repModel)


    def Update(self, model, ID):
        repModel = self.GetModelRepresentation(model)
        self.__context.UpdateRow(ID, repModel)


    def Delete(self, ID):
        self.__context.DeleteRow(ID)


    def GetModelRepresentation(self, model):
        return [model.Name, model.Proteins, model.Fats]