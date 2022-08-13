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


holder_name = str(dt_today.strftime('%Y-%m'))
holder_name_FN = str(dt_today.strftime('%Y-%m')) + '(FN)'
holder_name_Suehiro = str(dt_today.strftime('%Y-%m')) + '(Suehiro)'

getting_id()


seikyusho_id = holder_list["請求書"]
suehiro_id = holder_list["スエヒロ"]
foodnetwork_id = holder_list["foodnetwork"]
holder_name_FN_id = holder_list[holder_name_FN]
holder_name_Suehiro_id = holder_list[holder_name_Suehiro ]


if holder_name_Suehiro in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': holder_name_Suehiro,
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

# target_id = holder_list[holder_name]

def moving_google_drive(rename,title) :
   f = drive.CreateFile({"parents": [{"id": holder_name_Suehiro_id}]})
   f.SetContentFile(rename)
   f['title'] = title
   f.Upload()

if playing_date == 13:
  rename = main.get_receipt("microsoft")
  moving_google_drive(rename, "microsoft")

  