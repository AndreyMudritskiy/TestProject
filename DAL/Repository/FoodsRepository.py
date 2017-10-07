from DAL.DomainModel.Food import Food

class FoodsRepository:

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
        repModel = self.__GetModelRepresentation(model)
        return self.__context.InsertRow(repModel)


    def Update(self, model, ID):
        repModel = self.__GetModelRepresentation(model)
        self.__context.UpdateRow(ID, repModel)


    def Delete(self, ID):
        self.__context.DeleteRow(ID)


    def __GetModelRepresentation(self, model):
        return [model.Name, model.Proteins, model.Fats]