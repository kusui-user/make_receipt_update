import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import datetime
import main

os.chdir(os.path.dirname(os.path.abspath(__file__)))


dt_today = datetime.datetime.now()

playing_date = dt_today.day


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()


holder_list = {}


def getting_id():
    for f in file_list:
        holder_list[f['title']] = f['id']


getting_id()

if 'foodnetwork' in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': 'foodnetwork',
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

seikyusho_id = holder_list["請求書"]
suehiro_id = holder_list["スエヒロ"]
foodnetwork_id = holder_list["foodnetwork"]

holder_name2 = str(dt_today.strftime('%Y-%m')) + '(FN)'
holder_name3 = str(dt_today.strftime('%Y-%m')) + '(Suehiro)'

print(holder_name3)

# print(holder_list)
# print(suehiro_id)

# f = drive.CreateFile({"parents": [{"id": foodnetwork_id}]})
# f.SetContentFile(r'C:\Users\kusui\Desktop\DSCN5057.JPG')
# f['title'] = '請求書'
# f.Upload()



# def moving_google_drive(rename,title) :
#    f = drive.CreateFile({"parents": [{"id": seikyusho_id}]})
#    f.SetContentFile(rename)
#    f['title'] = title
#    f.Upload()

# if playing_date == 13:
#   rename = main.get_receipt("microsoft")
#   moving_google_drive(rename, "microsoft")