#google sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('database_creds.json', scope)
client = gspread.authorize(creds)

#get data from database
def request():
    #access google sheets database
    database = client.open("organizedData").get_worksheet(0)
    data = database.get_all_records()
    return data

#counters
def count(data) :
    #recyclable items
    recycle = data[0]["Amount"]
    #compostable items
    compost = data[1]["Amount"] 
    #landfill items
    landfill = data[2]["Amount"]
    #updates sheets
    return recycle, compost, landfill

#update google sheets
def update(r, c, l, category=""):
    if category == "R": r += 1
    elif category == "O": c += 1
    elif category == "L": l += 1

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

