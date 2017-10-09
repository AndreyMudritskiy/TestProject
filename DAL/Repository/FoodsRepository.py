from DAL.DomainModel.Food import Food
from DAL.Dataprovider.GoogleSheets.GoogleSheetsConnector import GoogleSheetsConnector

class FoodsRepository:

    def __init__(self):
        self.__conector = GoogleSheetsConnector()
        self.__context = self.__conector.GetInit().sheet1

    def Get(self, ID):
        listobj = self.__context.row_values(ID)
        model = Food()
        model.Name = listobj[0]
        model.Proteins = listobj[1]
        model.Fats = listobj[2]

        if model.IsEmpty() : return None

        return model


    def Insert(self, model):
        ID = len(self.__context.get_all_records()) + 2
        rmodel = self.__GetModelRepresentation(model)
        self.__context.insert_row(rmodel, ID)
        return ID


    def Update(self, model, ID):
        self.__context.update_cell(ID, 1, model.Name)
        self.__context.update_cell(ID, 2, model.Proteins)
        self.__context.update_cell(ID, 3, model.Fats)



    def Delete(self, ID):
        self.__context.delete_row(ID)


    def __GetModelRepresentation(self, model):
        return [model.Name, model.Proteins, model.Fats]