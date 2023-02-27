import datetime

today = datetime.datetime.now()

x = datetime.timedelta(5)

fdb = today - x

print(today)
print(fdb)