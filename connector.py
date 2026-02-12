import gspread
#install dependancies gspread (g sheet library) + oauth2client (auth w service account json)

gc = gspread.service_account(filename = 'service-account.json')
sheet = gc.open("WeeklyTutorFeedback").sheet1
data = sheet.get_all_records()
print(data)
