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

def getting_id():
    for f in file_list:
        holder_list[f['title']] = f['id']
    return holder_list[holder_name_ymd]

def fax_transfer_drive (file):
  f = drive.CreateFile({"parents": [{"id": fax_id}]})
  f.SetContentFile(file)
  # f['title'] = title
  f.Upload()

def fax_checking ():
  if not os.path.exists(path):
    os.mkdir(path)
  #   pass
  # else:
  #   os.mkdir(path)
  



if holder_name_ymd in holder_list:
   print('aruyo')
else:
   f = drive.CreateFile({'title': holder_name_ymd,
                              'mimeType': 'application/vnd.google-apps.folder'})
   f.Upload()
   print('tsukutayo')

for file in share.glob("*.pdf"):
    
    shutil.copy(file, path)
    shutil.move(file, fax_pdf)

# for file in fax_pdf.glob("*.pdf"):
#   fax_transfer_drive(file)


for item in os.listdir(fax_pdf):
        
       if item.endswith('.pdf'):
         fax_id = getting_id()
         fax_transfer_drive(item)
       











