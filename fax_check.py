import schedule
import time
import pathlib
import shutil
import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import datetime

dt_today = datetime.datetime.now()
holder_name_ymd = dt_today.strftime('%Y-%m-%d')+ '(fax-check)'
share = pathlib.WindowsPath(r'\\SUEHIRO\scan\SCAN')
fax_pdf = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\FAX-PDF\\'
path = r'C:\Users\kusui\OneDrive\デスクトップ\FAX-PDF\fax' + str(holder_name_ymd)


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()
holder_list = {}
fax_id = ''

def getting_id():
    for f in file_list:
        holder_list[f['title']] = f['id']
    

def fax_transfer_drive (file):
  fax_id = holder_list[holder_name_ymd]
  f = drive.CreateFile({"parents": [{"id": fax_id}]})
  f.SetContentFile(file)
  # f['title'] = title
  f.Upload()

getting_id()

def fax_checking ():
  print('スタートします')
  if not os.path.exists(path):
    os.mkdir(path)

  if not holder_name_ymd in holder_list:
     f = drive.CreateFile({'title': holder_name_ymd,
                              'mimeType': 'application/vnd.google-apps.folder'})
     f.Upload()
     getting_id()
     time.sleep(300)
  
  for file in share.glob("*.pdf"):
    shutil.move(file, fax_pdf)
  


  for item in os.listdir(fax_pdf):   
       if item.endswith('.pdf'):
         item = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\FAX-PDF\\' + item
         fax_transfer_drive(item)
         shutil.move(item, path)

def shutdown():
  os.system('shutdown -s')
  
schedule.every(10).minutes.do(fax_checking)
schedule.every().day.at("17:20").do(shutdown)

while True:
    schedule.run_pending()
    time.sleep(1)








