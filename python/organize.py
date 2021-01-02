#access txtfile
f = open('python\list.txt',"r")

data = f.read()

#parse txtfile

#-counters
#-------recyclable items
recycle = data.count("recycable")

#-------compostable items
compost = data.count("organic")

#-------landfill items
landfill = data.count("trash")


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

#excel sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('python\creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open("organizedData").sheet1

#data = sheet.get_all_records()
#pprint(data)

#update google sheets
sheet.update_cell(2,2, recycle)
sheet.update_cell(3,2, compost)
sheet.update_cell(4,2, landfill)