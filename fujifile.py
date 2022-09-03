from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import shutil
import sum

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

    driver.find_element(By.NAME, value="IDButton").click()
    driver.implicitly_wait(10)

    driver.find_element(By.CLASS_NAME, value="menuInfo").click()
    driver.implicitly_wait(10)
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="ebillingDownload"]/a').click()
    sleep(2)

    

    

    rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\富士フィルム.pdf'


    for item in sum.targetPath.glob('*.pdf'):
        item2 = item.rename(rename)
        item3 = shutil.move(item2, sum.moved_folder_suehiro )
        sum.printout(item3)
    return item3
        
        

