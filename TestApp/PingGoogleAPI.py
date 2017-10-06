from DAL.Dataprovider.GoogleSheets.GoogleSheetsConnector import GoogleSheetsConnector

db = GoogleSheetsConnector()
sheet = db.sheet1
print(sheet.row_values(2))



