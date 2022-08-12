import imapclient
from backports import ssl
from OpenSSL import SSL
import pyzmail
import os
import datetime
from slackweb import Slack
from dotenv import load_dotenv
import shutil

load_dotenv()


dt_now = datetime.datetime.now()
ym = dt_now.strftime('%Y-%m-%d-%S')
holder_name = dt_now.strftime('%Y-%m-%d')
date_term = datetime.timedelta(days=20)
target_date = dt_now - date_term
doing_day =dt_now.day

my_mail = "kusui@foodnetwork.co.jp"
app_password = "pxgqmakzutkdffdq"

slacks =os.getenv('slack')

slack =Slack(slacks)


mail_list = {"google": "payments-noreply@google.com",
             "amazon": "no-reply@amazon.com",
             "microsoft": "microsoft-noreply@microsoft.com",
             "iizuka": "kumiko.sata@orchestra-ac.com"
             }

context = ssl.SSLContext(SSL.TLSv1_2_METHOD)
imap = imapclient.IMAPClient("imap.gmail.com", ssl=True, ssl_context=context)
imap.login(my_mail, app_password)

folder = r'C:\Users\kusui\OneDrive\デスクトップ\folder'
path = r'C:\Users\kusui\OneDrive\デスクトップ\folder\top' + str(holder_name)

if os.path.exists(path):
  pass
else:
  os.mkdir(path)

def get_receipt (company):
    imap.select_folder("INBOX", readonly=True)
    KWD = imap.search(["SINCE", target_date, "FROM", mail_list[company]])
    raw_message = imap.fetch(KWD, ["BODY[]"])


    i = 0
    

    for j in range(len(KWD)):

        # 特定メール取得
        message = pyzmail.PyzMessage.factory(raw_message[KWD[j]][b"BODY[]"])
        for part in message.walk():
            file_name = part.get_filename()
            if not file_name:
                continue

            with open(f'{folder}/{file_name}', 'wb') as f:
                f.write(part.get_payload(decode=True))

    folder1 = os.listdir(folder)
    
    for item in folder1:
        rename = "C:\\Users\\kusui\\OneDrive\\デスクトップ\\folder\\" + company + str(ym) + str(i) + '.pdf'
        os.rename(f"{folder}/{item}", rename)
        if item.endswith('.pdf'):
            shutil.move(rename, path)
        i = i + 1 
    slack.notify(text="amazon請求書を取得しました")

if doing_day == 3:
    # get_receipt("google")
    get_receipt("iizuka")
elif doing_day == 2:
    get_receipt("google")

else:
    print("no")





