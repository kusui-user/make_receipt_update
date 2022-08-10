import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import datetime
from popup import sayhello




dt_today = datetime.datetime.now()

playing_date = dt_today.day

os.chdir(os.path.dirname(os.path.abspath(__file__)))

 
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()
file_list_number = len(file_list)

holder_list = {}

def getting_id () :
  for f in file_list:
    holder_list[f['title']] = f['id']
    # print(f['title'])
    
    
holder_name = str(dt_today.strftime('%Y-%m-%d'))

# print(file_list[13]['title'])

# for n in range(file_list_number):
#   print(file_list[n]['title'])
  
#   if holder_name in file_list[n]['title'] :
#     print('get it')


# if playing_date == 10:
#   for n in range(file_list_number):
#     if not holder_name in file_list[n]['title'] :
#       getting_id ()
#       print('oruyo')
    
#     else:
      # f = drive.CreateFile({'title': holder_name,
      #                       'mimeType': 'application/vnd.google-apps.folder'})
      # f.Upload()
#       getting_id ()
#       print('Naiyo')
# else:
#   getting_id ()

if playing_date == 10:
   getting_id()
  #  print(holder_list)
   
   if holder_name in holder_list:
     print('oruyo')
   else:
     f = drive.CreateFile({'title': holder_name,
                            'mimeType': 'application/vnd.google-apps.folder'})
     f.Upload()
     print('tsukutayo')


# target_id = holder_list[holder_name]


# f = drive.CreateFile({"parents": [{"id": target_id}]})
# f.SetContentFile(r'C:\Users\kusui\Desktop\DSCN5057.JPG')
# f['title'] = 'picture.jpg'
# f.Upload()

# file_list2 = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(target_id)}).GetList()

# for f in file_list2:
#     print(f['title'], ' \t', f['id'])

sayhello()







# if os.path.exists(holder_name):
#   pass
# else:
#   f = drive.CreateFile({'title': holder_name,
#                       'mimeType': 'application/vnd.google-apps.folder'})
  # f.SetContentString('new text')
  # f.Upload()




# print(type(file_list[1]))


# for f in file_list:
#     print(f['title'], '   \t', f['id'])
    
# folder_id = drive.ListFile({'q': 'title = holder_name '}).GetList()[0]['id']

# f = drive.CreateFile({"parents": [{"id": folder_id}]})
# f.SetContentFile(r'C:\Users\kusui\Desktop\DSCN5057.JPG')
# f['title'] = 'picture.jpg'
# f.Upload()