from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
import shutil



USERID =[ "048924630003", "048924630033", "036265690502"]
PASSWORD ="ginza444"

options = webdriver.EdgeOptions()

download = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download'

# ブラウザを非表示視するオプション
# options.add_argument('--headless')
options.add_experimental_option("prefs", {"download.default_directory": download })
driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install()),
    options=options
)

yamato_list = []




def yamato():
    i = 0
    while i < 3:
        driver.get("https://bmypage.kuronekoyamato.co.jp/bmypage/jsp/webbill.jsp")
        driver.find_element(By.NAME, "CSTMR_CD").send_keys(USERID[i])
        driver.implicitly_wait(10)

        driver.find_element(By.NAME, "CSTMR_PSWD").send_keys(PASSWORD)
        driver.implicitly_wait(10)
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="loginbutton"]/a').click()
        driver.implicitly_wait(10)
        sleep(1)

        driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/table[2]/tbody/tr[1]/td[2]/a').click()
        driver.implicitly_wait(10)
        sleep(1)

        driver.find_element(By.ID, 'BILL_DOWNLOAD').click()
        driver.implicitly_wait(10)
        sleep(1)

        rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\ヤマト' + str(i) + '.pdf'

        for item in targetPath.glob('*.pdf'):
            item2 = item.rename(rename)

            item3 = shutil.move(item2, sum.moved_folder )
            yamato_list.append(item3)
            sum.printout(item3)
            

        driver.find_element(By.ID, 'DETAIL_DOWNLOAD').click()
        driver.implicitly_wait(10)
        sleep(2)


        targetPath = Path('C:\\Users\\kusui\\OneDrive\\デスクトップ\\download')
        rename_sc = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\ヤマト' + str(i) + '-2.pdf'
    


        for ite in targetPath.glob('*.pdf'):
            item_sc = ite.rename(rename_sc)
            item_sc_n = shutil.move(item_sc, sum.moved_folder )
            yamato_list.append(item_sc_n)
            # conf_file_path = item_sc_n
            sum.printout(item_sc_n)
            

        
        driver.find_element(By.XPATH, '//*[@id="topicpath-area"]/p/a').click()
        driver.implicitly_wait(10)
        sleep(2)
        i += 1
 
     
    return yamato_list

print(yamato_list)








