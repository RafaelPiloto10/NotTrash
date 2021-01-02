#google sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('python\creds.json', scope)

client = gspread.authorize(creds)

#access google sheets database
database = client.open("organizedData").get_worksheet(2)

data = database.get_all_records()

pprint(data)

#access txtfile
#f = open('python\list.txt',"r")

#data = f.read()

#parse txtfile

#-counters
#-------recyclable items
recycle =  sum([1 for i in range(len(data)) if data[i]["Classification"] == 'recycable'])

#-------compostable items
compost = sum([1 for i in range(len(data)) if data[i]["Classification"] == 'organic'])

#-------landfill items
landfill = sum([1 for i in range(len(data)) if data[i]["Classification"] == 'trash'])


#print items
#-------recyclable items
print('recycable:', recycle)

#-------compostable items
print('compostable:', compost)

#-------landfill items
print('landfill:', landfill)

#list
alldata = []
alldata.append(recycle)
alldata.append(compost)
alldata.append(landfill)

print(alldata)

#update google sheets
sheet = client.open("organizedData").sheet1

data2 = sheet.get_all_records()

pprint(data2)

sheet.update_cell(2,2, recycle)
sheet.update_cell(3,2, compost)
sheet.update_cell(4,2, landfill)