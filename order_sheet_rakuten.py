# from asyncore import file_dispatcher
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pathlib import Path
import sum

from datetime import datetime, date, timedelta

from selenium.webdriver.common.keys import Keys

today = datetime.today()


before_7day = today - timedelta(days=7)
yesterday = today - timedelta(days=1)

start_date =datetime.strftime(before_7day, '%Y-%m-%d') 
end_date =datetime.strftime(yesterday, '%Y-%m-%d') 

USERID ="g4suehiro"
PASSWORD ="Suehiro444"

USERID_person ="kusui.takashi@gmail.com"
PASSWORD_person ="Tkusui4860@"

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

    driver.find_element(by=By.ID, value="rms-checkbox-order-header-checkbox").click()#全選択チエック

    driver.find_element(By.CLASS_NAME, value="rms-collapse-button").click()#一括処理


    driver.find_element(by=By.ID, value="btnFormCreation").click()#作成ボタン
    driver.find_element(by=By.ID, value="pdfOpen").click()#pdfを開くボタン
    driver.find_element(by=By.ID, value="icon").click()#pdfを開くボタン
    sleep(100)

    

    # driver.switch_to.frame(driver.find_element(By.ID, value="embeddedIframe"))
    # driver.implicitly_wait(10)
    # driver.find_element(By.CLASS_NAME, value="btnBill").click()
    # sleep(2)


    # driver.implicitly_wait(10)
    # sleep(2)

    # targetPath = Path('C:\\Users\\kusui\\OneDrive\\デスクトップ\\download')
    # rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\download\\ソフトバンク.pdf'
    # moved_folder = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\請求書\\' + str(sum.ym)

    
    # for item in targetPath.glob('*.pdf'):
    #     item2 = item.rename(rename)
    #     item3 = shutil.move(item2, moved_folder )
    #     # conf_file_path = file
    #     sum.printout(item3)
        
    #     return item3





    
      
order_sheet ()