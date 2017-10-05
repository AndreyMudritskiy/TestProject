import gspread
from oauth2client.service_account import ServiceAccountCredentials

url = ['https://spreadsheets.google.com/feeds']
secret = ServiceAccountCredentials.from_json_keyfile_name(r'client_secret.json', url)
client = gspread.authorize(secret)

sheet = client.open('products').sheet1

animals = sheet.get_all_records();
print(animals)

print(sheet.row_values(3))
