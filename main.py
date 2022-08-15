import imapclient
from backports import ssl
from OpenSSL import SSL
import pyzmail
import os
# import datetime
from slackweb import Slack
from dotenv import load_dotenv
import shutil
import sum


load_dotenv()


# dt_now = datetime.datetime.now() #main_remake 変数あり 
# ym = dt_now.strftime('%Y-%m-%d-%S') #main_remake 変数ありymds
# holder_name = dt_now.strftime('%Y-%m-%d')#main_remake 変数ありholder_name_ymd
# date_term = datetime.timedelta(days=20)
# target_date = dt_now - date_term
# doing_day =dt_now.day

my_mail = "kusui@foodnetwork.co.jp"



slacks =os.getenv('slack')
app_password  = os.getenv('app_password')

slack =Slack(slacks)


mail_list = {"google": "payments-noreply@google.com",
             "amazon": "no-reply@amazon.com",
             "microsoft": "microsoft-noreply@microsoft.com",
             "iizuka": "kumiko.sata@orchestra-ac.com"
             }

context = ssl.SSLContext(SSL.TLSv1_2_METHOD)
imap = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
imap.login(my_mail, app_password)

# folder = r'C:\Users\kusui\OneDrive\デスクトップ\folder'
# folder_home = r'C:\Users\kusui\Desktop\folder'
# path = r'C:\Users\kusui\OneDrive\デスクトップ\folder\recipt' + str(holder_name)
# path_home = r'C:\Users\kusui\Desktop\folder\recipt' + str(holder_name)

if os.path.exists(sum.path):
  pass
else:
  os.mkdir(sum.path)

def get_receipt (company):
    imap.select_folder("INBOX", readonly=True)
    KWD = imap.search(["SINCE", sum.target_date, "FROM", mail_list[company]])
    raw_message = imap.fetch(KWD, ["BODY[]"])

    i = 0
    
    for j in range(len(KWD)):

        # 特定メール取得
        message = pyzmail.PyzMessage.factory(raw_message[KWD[j]][b"BODY[]"])
        for part in message.walk():
            file_name = part.get_filename()
            if not file_name:
                continue

            with open(f'{sum.folder}/{sum.file_name}', 'wb') as f:
                f.write(part.get_payload(decode=True))

    for item in os.listdir(sum.folder):
        rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\folder\\' + company + str(sum.ymds) + str(i) + '.pdf'
        rename_home = 'C:\\Users\\kusui\\Desktop\\folder\\' + company + str(sum.ymds) + str(i) + '.pdf'
        if item.endswith('.pdf'):
            os.rename(f"{sum.folder}/{item}", rename)
            # shutil.move(rename, path)
            return rename
    
        i = i + 1 
        
    # slack.notify(text="amazon請求書を取得しました")







