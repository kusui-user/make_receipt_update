from datetime import datetime, date, timedelta
import shutil
import os
import sum
import pathlib
dowload_folder = r'C:\\Users\\kusui\\Downloads\\'

today = datetime.today()


before_7day = today - timedelta(days=7)
yesterday = today - timedelta(days=1)
ym = today.strftime('%Y.%m')

start_date =datetime.strftime(before_7day, '%Y.%m.%d') 
end_date =datetime.strftime(yesterday, '%d') 

file_name = "楽天" + start_date + "-" + end_date
file_name2 = start_date + "-" + end_date + ".pdf"

# share = pathlib.WindowsPath(f'\\SUEHIRO\\open\\注文書\\スエヒロ\\{sum.y}\\{ym}\\楽天')
Open_folder = pathlib.WindowsPath(r'\\SUEHIRO\open\\注文書\\スエヒロ\\{}\\{}\\楽天' .format(sum.y, ym))
# share = pathlib.WindowsPath(r'\\SUEHIRO\\open\\注文書\\スエヒロ\\2022\\{}\\楽天' .format(ym))
share2 = pathlib.WindowsPath(r'\\SUEHIRO\scan\SCAN')



# print( datetime.strftime(before_7day, '%Y-%m-%d'))
# print("昨日 -> " + datetime.strftime(yesterday, '%Y-%m-%d'))

print(share)
print(file_name2)

# for file in dowload_folder.glob("*.pdf"):
#   shutil.move(f"{dowload_folder}/{file}", share2)
  # print(file)
    # shutil.move(file, fax_pdf)


for item in os.listdir(dowload_folder ):   
       if item.endswith(file_name2 ):
        print('OK')
        shutil.move(f"{dowload_folder}/{item}", share)
       else:
        print('NO')






