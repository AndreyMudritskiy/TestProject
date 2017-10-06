import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheetsConnector(object):

    _instance = None

    def __new__(self):
        if not self._instance:
            self._instance = GoogleSheetsConnector()
            self.Init()

        return self._instance


    def Init(self):

        url = ['https://spreadsheets.google.com/feeds']
        secret = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', url)
        client = gspread.authorize(secret)
        _Dbcontext = client.open("products")


