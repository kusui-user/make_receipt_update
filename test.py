# from asyncore import file_dispatcher
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
import shutil
import sum

USERID ="e-shop@g4-suehiro.jp"
PASSWORD ="Suehiro44593"


options = webdriver.EdgeOptions()
download = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download'

    # ブラウザを非表示視するオプション
    # options.add_argument('--headless')
options.add_experimental_option("prefs", {"download.default_directory": download })
driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

driver.get("https://webmeisai.itc.softbank.jp")


driver.find_element(by=By.ID, value="login").send_keys(USERID)
driver.implicitly_wait(10)
driver.find_element(by=By.ID, value="password").send_keys(PASSWORD)
driver.implicitly_wait(10)
sleep(1)

# import sys
# sys.base_prefix



