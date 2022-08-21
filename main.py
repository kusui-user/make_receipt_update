import imapclient
from backports import ssl
from OpenSSL import SSL
import pyzmail
import os
from slackweb import Slack
from dotenv import load_dotenv
import sum
import imaplib
import email



load_dotenv()


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


if os.path.exists(sum.path_home):
  pass
else:
  os.mkdir(sum.path_home)

def get_receipt (company):
    imap.select_folder("INBOX", readonly=True)
    KWD = imap.search(["SINCE", sum.target_date, "FROM", mail_list[company]])
    raw_message = imap.fetch(KWD, ["BODY[]"])

    i = 0
    
    attachments = []
    
    for j in range(len(KWD)):

        # 特定メール取得
        message = pyzmail.PyzMessage.factory(raw_message[KWD[j]][b"BODY[]"])
        for part in message.walk():
            file_name = part.get_filename()
            
            
            if not file_name:
                continue
            
            

            with open(f'{sum.folder_home}/{file_name}', 'wb') as f:
                f.write(part.get_payload(decode=True))


    for item in os.listdir(sum.folder_home):
        # rename = 'C:\\Users\\kusui\\OneDrive\\デスクトップ\\folder\\' + company + str(sum.ymds) + str(i) + '.pdf'
        rename_home = 'C:\\Users\\kusui\\Desktop\\folder\\' + company + str(sum.ymds) + str(i) + '.pdf'
        if item.endswith('.pdf'):
            os.rename(f"{sum.folder_home}/{item}", rename_home)
            # shutil.move(rename, path)
            return rename_home
    
        i = i + 1 
        
    # slack.notify(text="amazon請求書を取得しました")


get_receipt("iizuka")




