import datetime

year = int(input())
month = int(input())
day = int(input())
hour = int(input())
minute = int(input())
second = int(input())

y1,m1,d1,h1,minu1,sec1 = int(input()),int(input()),int(input()),int(input()),int(input()),int(input())
#x = datetime.datetime(2013,12,30,23,59,59)
x = datetime.datetime(year, month, day, hour, minute, second)
#y = datetime.datetime(2013,12,31,23,59,59)
y = datetime.datetime(y1,m1,d1,h1,minu1,sec1)
print((y-x).total_seconds())