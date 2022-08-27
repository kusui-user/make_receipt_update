import win32gui
import win32.lib.win32con as win32con
memo_app = win32gui.FindWindow(None,'d5d7097ea16b705da1d4d1b0ebe63572.pdf - 職場 - Microsoft​ Edge')    #「タイトルなし - メモ帳」という名前のウィンドウハンドルを取得
win32gui.SetForegroundWindow(memo_app)                         #ウィンドウを最前面に移動してアクティブ化
win32gui.ShowWindow(memo_app, win32con.SW_MAXIMIZE) 



