from datetime import datetime, date, timedelta

today = datetime.today()


before_7day = today - timedelta(days=7)
yesterday = today - timedelta(days=1)

start_date =datetime.strftime(before_7day, '%Y-%m-%d') 
end_date =datetime.strftime(yesterday, '%Y-%m-%d') 

# print( datetime.strftime(before_7day, '%Y-%m-%d'))
# print("昨日 -> " + datetime.strftime(yesterday, '%Y-%m-%d'))

print(start_date)
print(end_date)