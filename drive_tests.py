import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
# import datetime
import main
import shutil
import softbank
import fujifile
import rakuten
import yamato
import sum


os.chdir(os.path.dirname(os.path.abspath(__file__)))


# dt_today = datetime.datetime.now()
# ym = dt_today.strftime('%Y-%m')

# playing_date = dt_today.day


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()



holder_list = {}

def getting_id():
    for f in file_list:
        holder_list[f['title']] = f['id']


# holder_name = str(dt_today.strftime('%Y-%m'))
# holder_name_FN = str(dt_today.strftime('%Y-%m')) + '(FN)'
# holder_name_Suehiro = str(dt_today.strftime('%Y-%m')) + '(Suehiro)'
# moved_folder = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書(FN)\\' + str(ym)

getting_id()

#フォルダーid
seikyusho_id = holder_list["請求書"]
suehiro_id = holder_list["スエヒロ"]
foodnetwork_id = holder_list["foodnetwork"]
holder_name_FN_id = holder_list[sum.holder_name_FN]
holder_name_Suehiro_id = holder_list[sum.holder_name_Suehiro ]


if sum.holder_name_Suehiro in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': sum.holder_name_Suehiro,
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

if sum.holder_name_FN in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': sum.holder_name_FN,
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

# target_id = holder_list[holder_name]

def moving_google_drive(rename,title,id) :
   f = drive.CreateFile({"parents": [{"id": id}]})
   f.SetContentFile(rename)
   f['title'] = title
   f.Upload()

if sum.playing_date == 1:
  rename = main.get_receipt("microsoft")
  moving_google_drive(rename, "microsoft", holder_name_FN_id)
  shutil.move(rename, sum.moved_folder)

elif sum.playing_date == 3:
  rename = main.get_receipt("amazon")
  moving_google_drive(rename, "amazon", holder_name_FN_id)
  shutil.move(rename, sum.moved_folder)

elif sum.playing_date == 5:
  rename = main.get_receipt("google")
  moving_google_drive(rename, "google", holder_name_FN_id)
  shutil.move(rename, sum.moved_folder)

elif sum.playing_date == 6:
  rename = softbank.softbank()
  moving_google_drive(rename, "softbank", holder_name_Suehiro_id)

elif sum.playing_date == 7:
  rename = fujifile.fujifile()
  moving_google_drive(rename, "fujifile", holder_name_Suehiro_id)

elif sum.playing_date == 8 or 28:
  rename = rakuten.rakuten()
  print(rename)

  moving_google_drive(rename[0], "rakuten", holder_name_FN_id)
  moving_google_drive(rename[1], "rakuten", holder_name_Suehiro_id)

elif sum.playing_date == 14:
  rename = yamato.yamato()
  print(rename)

  for index,name in enumerate(rename) :
    moving_google_drive(rename[index], "yamato"+ str(index), holder_name_Suehiro_id)

 


  



  