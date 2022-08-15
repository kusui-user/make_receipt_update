from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from pathlib import Path
import shutil
# import datetime
import os
import win32api
import win32print
import sum

# dt_now = datetime.datetime.now()
# ym = dt_now.strftime('%Y-%m')
USERID ="e-shop@g4-suehiro.jp"
PASSWORD ="suehiro444"

def fujifile():
    options = webdriver.EdgeOptions()
    download = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download'

    # ブラウザを非表示視するオプション
    # options.add_argument('--headless')
    options.add_experimental_option("prefs", {"download.default_directory": download })
    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

    driver.get("https://sso-web-fb.fujifilm.com/direct/ebilling/")



    driver.find_element(by=By.ID, value="IDToken1").send_keys(USERID)
    driver.implicitly_wait(10)

    driver.find_element(by=By.ID, value="IDToken2").send_keys(PASSWORD)
    driver.implicitly_wait(10)

    driver.find_element(By.NAME, "IDButton").click()
    driver.implicitly_wait(10)

    driver.find_element(By.CLASS_NAME, "menuInfo").click()
    driver.implicitly_wait(10)

    driver.find_element(By.ID, 'ebillingDownload').click()
    sleep(2)

    # targetPath = Path('C:\\Users\\kusui\\OneDrive\\デスクトップ\\download')
    rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\富士フィルム.pdf'
    # moved_folder = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書\\' + str(sum.ym)



    for item in sum.targetPath.glob('*.pdf'):
        item2 = item.rename(rename)
        item3 = shutil.move(item2, sum.moved_folder )
        conf_file_path = item3
        win32api.ShellExecute(
            0,
            "print",
            conf_file_path,
            "/c:""%s" % win32print.GetDefaultPrinter(),
            ".",
            0
                )
    return item3
        
        

