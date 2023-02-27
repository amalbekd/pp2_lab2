import datetime

today = datetime.datetime.now()
day = datetime.timedelta(1)
yesterday = today - day
tomorrow = today + day
print(yesterday)
print(today)
print(tomorrow)