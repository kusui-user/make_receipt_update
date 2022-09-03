
import datetime
from tkinter import Y
from dotenv import load_dotenv
from pathlib import Path
import win32api
import win32print




load_dotenv()

#変数
dt_today = datetime.datetime.now()
y=dt_today.strftime('%Y')
ym = dt_today.strftime('%Y-%m')
ymds = dt_today.strftime('%Y-%m-%d-%S')
ymd = dt_today.strftime('%Y-%m-%d')
md = dt_today.strftime('%m-%d')
date_term = datetime.timedelta(days=20)
target_date = dt_today - date_term
doing_day =dt_today.day
playing_date = dt_today.day


#holder name
holder_name = str(dt_today.strftime('%Y-%m'))
holder_name_ymd = dt_today.strftime('%Y-%m-%d')
holder_name_FN = str(dt_today.strftime('%Y-%m')) + '(FN)'
holder_name_Suehiro = str(dt_today.strftime('%Y-%m')) + '(Suehiro)'


#保存場所
folder = r'C:\Users\kusui\OneDrive\デスクトップ\folder'
folder_home = r'C:\Users\kusui\Desktop\folder'
path = r'C:\Users\kusui\OneDrive\デスクトップ\folder\recipt' + str(holder_name)
path_home = r'C:\Users\kusui\Desktop\folder\recipt' + str(holder_name)

# moved_folder = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書(FN)\\' + str(ym)#moved_folder_food同じ
targetPath = Path('C:\\Users\\kusui\\OneDrive\\デスクトップ\\download')
moved_folder_food = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書(FN)\\' + str(ym)
moved_folder_suehiro = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書\\' + str(ym)


def printout(file):
  conf_file_path = file
  win32api.ShellExecute(
            0,
            "print",
            conf_file_path,
            "/c:""%s" % win32print.GetDefaultPrinter(),
            ".",
            0
                )
  











 


  



  