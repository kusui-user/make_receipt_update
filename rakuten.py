from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
# import pathlib
import shutil
# import datetime
import os
import win32api
import win32print

# dt_now = datetime.datetime.now()
# ym = dt_now.strftime('%Y-%m')
# md = dt_now.strftime('%m-%d')
USERID =["3000123971","3000181665"]
PASSWORD =["sunnet98769", "ginza4Suehiro10"]
rakuten_list = []

def rakuten():
    options = webdriver.EdgeOptions()
    download = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download'

    # ブラウザを非表示視するオプション
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", {"download.default_directory": download })
    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

    i = 0

    

    while i < 2:

        driver.get("https://billpay.rakuten.co.jp/login")
        driver.find_element(by=By.ID, value="userId").send_keys(USERID[i])
        driver.implicitly_wait(10)

        driver.find_element(by=By.ID, value="password").send_keys(PASSWORD[i])
        driver.implicitly_wait(10)

        driver.find_element(By.NAME, "doLogin").click()
        driver.implicitly_wait(10)
        sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[1]/main/nav/form/div/ul/li[3]/a").click()
        driver.implicitly_wait(10)
        sleep(3)

        driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/form/div[2]/table/tbody[1]/tr[5]/td/div[1]/div/button[1]').click()
        sleep(1)


        # targetPath = Path('C:\\Users\\kusui\\OneDrive\\デスクトップ\\download')
        rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\楽天' + str(sum.md) + '.pdf'
        # moved_folder_food = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書(FN)\\' + str(sum.ym)
        # moved_folder_suehiro = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書\\' + str(sum.ym)

        

        for item in sum.targetPath.glob('*.pdf'):
            item2 = item.rename(rename)
            
            if (i == 0):
                item3 = shutil.move(item2, sum.moved_folder_food )
                rakuten_list.append(item3)
                sum.printout(item3)
            
            elif(i == 1):
                item4 = shutil.move(item2, sum.moved_folder_suehiro )
                rakuten_list.append(item4)
                sum.printout(item4)
            else:
                break

        i += 1

    return rakuten_list








