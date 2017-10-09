import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


class GoogleSheetsConnector:

    def GetInit(self):

        url = ['https://spreadsheets.google.com/feeds']
        secret = ServiceAccountCredentials.from_json_keyfile_name(self.GetClientSecretPath(), url)
        client = gspread.authorize(secret)
        return client.open("products")

    def GetClientSecretPath(self):
        return os.path.dirname(os.path.realpath(__file__)) + '\client_secret.json'


