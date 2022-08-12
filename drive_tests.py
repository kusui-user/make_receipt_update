import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import datetime
import main


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

getting_id()

if holder_name in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': holder_name,
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

target_id = holder_list[holder_name]

def moving_google_drive(rename,title) :
   f = drive.CreateFile({"parents": [{"id": target_id}]})
   f.SetContentFile(rename)
   f['title'] = title
   f.Upload()

if playing_date == 12:
  rename = main.get_receipt("google")
  moving_google_drive(rename, "google")

  