import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsConnector(object):

    def GetInit(self):

        url = ['https://spreadsheets.google.com/feeds']
        secret = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', url)
        client = gspread.authorize(secret)
        return client.open("products")


