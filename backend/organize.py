#google sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('backend\creds.json', scope)
client = gspread.authorize(creds)

def request():
    #access google sheets database
    database = client.open("organizedData").get_worksheet(2)
    data = database.get_all_records()
    return data

#-counters
def count(data) :
    #recyclable items
    recycle =  sum([1 for i in range(len(data)) if data[i]["Classification"] == 'recycable'])
    #compostable items
    compost = sum([1 for i in range(len(data)) if data[i]["Classification"] == 'organic'])
    #landfill items
    landfill = sum([1 for i in range(len(data)) if data[i]["Classification"] == 'trash'])
    #updates sheets
    update(recycle, compost, landfill)
    return

#update google sheets
def update(r, c, l):
    sheet = client.open("organizedData").sheet1
    sheet.update_cell(2,2, r)
    sheet.update_cell(3,2, c)
    sheet.update_cell(4,2, l)
    #print items
    #recyclable items
    print('recycable:', r)
    #compostable items
    print('compostable:', c)
    #landfill items
    print('landfill:', l)
    return

count(request())
