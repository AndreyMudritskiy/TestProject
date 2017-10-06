from DAL.Dataprovider.GoogleSheets.GoogleSheetsConnector import GoogleSheetsConnector

class GoogleSheetsDataProvider:

    def GetRow(self, ID):
        db = GoogleSheetsConnector()
        sheet = db.sheet1
        return sheet.row_values(ID)

    def UpdRow(self, ID, model):
        db = GoogleSheetsConnector()
        sheet = db.sheet1
        sheet.insert_row(model, ID)

    def InsertRow(self, model):
        db = GoogleSheetsConnector()
        sheet = db.sheet1
        ID = sheet.row_count
        sheet.insert_row(model, ID)
        return ID


    def DeleteRow(self, ID):
        db = GoogleSheetsConnector()
        sheet = db.sheet1
        sheet.delete_row(ID)


# TODO: нужен мапинг таблиц