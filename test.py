# import win32gui
# import win32.lib.win32con as win32con
# memo_app = win32gui.FindWindow(None,'Adobe Acrobat Pro DC (32-bit)')    #「タイトルなし - メモ帳」という名前のウィンドウハンドルを取得
# win32gui.SetForegroundWindow(memo_app)                         #ウィンドウを最前面に移動してアクティブ化
# win32gui.ShowWindow(memo_app, win32con.SW_MAXIMIZE) 


import schedule
from time import sleep

def say_hello ():
  print('HELOO')

schedule.every().tuesday.at("10:19:00").do(say_hello) 

while True:
    schedule.run_pending()
    sleep(1) 
    



