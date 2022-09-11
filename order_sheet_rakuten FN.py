# from asyncore import file_dispatcher
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import sum
import shutil
import pyautogui as pag
import os
import pathlib
import schedule

from datetime import datetime, date, timedelta

from selenium.webdriver.common.keys import Keys

today = datetime.today()


before_7day = today - timedelta(days=7)
yesterday = today - timedelta(days=1)

start_date =datetime.strftime(before_7day, '%Y.%m.%d') 
end_date =datetime.strftime(yesterday, '%Y.%m.%d') 
end_date_dd =datetime.strftime(yesterday, '%d') 
file_name = start_date + "-" + end_date_dd + ".pdf"
dowload_folder = r'C:\\Users\\kusui\\Downloads\\'

USERID ="okazuippin"
PASSWORD ="okazutaku"

USERID_person ="kusui.takashi@gmail.com"
PASSWORD_person ="Tkusui4860@"

Open_folder = pathlib.WindowsPath(r'\\SUEHIRO\open\\注文書\\おかずや\\{}\\{}\\楽天' .format(sum.y, sum.ym))

def order_sheet () :
    options = webdriver.EdgeOptions()
    download = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download'

    # ブラウザを非表示視するオプション
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", {"download.default_directory": download })
    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

    driver.get("https://glogin.rms.rakuten.co.jp/?sp_id=1")

    driver.maximize_window()


    driver.find_element(by=By.ID, value="rlogin-username-ja").send_keys(USERID)
    driver.implicitly_wait(10)
    driver.find_element(by=By.ID, value="rlogin-password-ja").send_keys(PASSWORD)
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element(By.CLASS_NAME, value="rf-button-primary").click()
    
    driver.find_element(by=By.ID, value="rlogin-username-2-ja").send_keys(USERID_person)
    driver.implicitly_wait(10)
    driver.find_element(by=By.ID, value="rlogin-password-2-ja").send_keys(PASSWORD_person)
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element(By.CLASS_NAME, value="rf-button-primary").click()

    driver.find_element(By.CLASS_NAME, value="rf-button-primary").click()
    driver.find_element(By.CLASS_NAME, value="btn-reset").click()
    driver.find_element(By.CLASS_NAME, value="rms-ui-icon-cart-2").click()
    driver.find_element(By.XPATH, '//*[@id="com_gnavi0201"]/div').click()
    
    driver.find_element(by=By.ID, value="mm_sub0201_18").click()
    driver.implicitly_wait(10)


    driver.find_element(by=By.ID, value="orderProgressList5").click() #発送済チエック
    driver.find_element(by=By.ID, value="orderProgressList6").click() #支払手続き中チエック
    driver.find_element(by=By.ID, value="orderProgressList7").click() #支払手続き済チエック


    
    driver.find_element(by=By.ID, value="startDate").click
    driver.find_element(by=By.ID, value="startDate").clear
    for i in range(10):     
        driver.find_element(by=By.ID, value="startDate").send_keys(Keys.BACK_SPACE)
    driver.find_element(by=By.ID, value="startDate").send_keys(start_date)
    
    driver.find_element(by=By.ID, value="endDate").click
    driver.find_element(by=By.ID, value="endDate").clear
    for i in range(10):  
        driver.find_element(by=By.ID, value="endDate").send_keys(Keys.BACK_SPACE)
    driver.find_element(by=By.ID, value="endDate").send_keys(end_date)
    sleep(1)

    # driver.execute_script("window.scrollBy(0, 1000);")


    driver.find_element(by=By.ID, value="rms-content-save-button").click() #検索ボタン

    driver.find_element(By.XPATH, '//*[@id="ddlDisplay"]/option[5]').click()#300件選択
    sleep(1)

    driver.find_element(by=By.ID, value="rms-checkbox-order-header-checkbox").click()#全選択チエック

    driver.find_element(By.CLASS_NAME, value="rms-collapse-button").click()#一括処理

    driver.find_element(by=By.ID, value="btnFormCreation").click()#作成ボタン
    sleep(1)
    driver.find_element(by=By.ID, value="pdfOpen").click()#pdfを開くボタン
    sleep(30)
  

    pag.click(1236 ,178)
    sleep(5)

    # pag.click(1236 ,178)
    pag.press("backspace")
    sleep(1)

    pag.write(file_name)
    sleep(1)

    pag.click(223 ,376)
    sleep(1)
    
    pag.click(504 ,447)
    sleep(1)
    print('終わりました')

    for item in os.listdir(dowload_folder ):   
       if item.endswith(file_name ):
        print('OK')
        shutil.move(f"{dowload_folder}/{item}", Open_folder)
       else:
        print('NO')

order_sheet()

    


# schedule.every().monday.at("7:10").do(order_sheet) 

# while True:
#     schedule.run_pending()
#     sleep(1)    


      
