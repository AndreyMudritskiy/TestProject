from DAL.Dataprovider.GoogleSheets.GoogleSheetsConnector import GoogleSheetsConnector
from DAL.Dataprovider.IDataprovider import IDataprovider

class GoogleSheetsDataProvider(IDataprovider):

    def __init__(self):
        self.__db = GoogleSheetsConnector().GetInit()

    def GetRow(self, ID):
        sheet = self.__db.sheet1
        return sheet.row_values(ID)

    def UpdateRow(self, ID, model):
        sheet = self.__db.sheet1

        sheet.update_cell(ID, 1, model[0])
        sheet.update_cell(ID, 2, model[1])
        sheet.update_cell(ID, 3, model[2])

    def InsertRow(self, model):

        sheet = self.__db.sheet1
        "#ID = sheet.row_count   # отдает конец таблицы с пустыми строками"
        ID = len(sheet.get_all_records()) + 2   # колекция начинается с нул и нужно взять новую строчку.
        sheet.insert_row(model, ID)
        return ID

    def DeleteRow(self, ID):
        sheet = self.__db.sheet1
        sheet.delete_row(ID)


# TODO: нужен мапинг таблиц