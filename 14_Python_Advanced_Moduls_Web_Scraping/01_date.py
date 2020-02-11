from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

# result = dir(datetime)
# print(result)

simdi = datetime.now()
print(simdi)
print(simdi.day)
print(simdi.month)
print(simdi.year)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)

print("today kullanımı now ile aynıdır")
simdi = datetime.today()
print(simdi)
print(simdi.day)
print(simdi.month)
print(simdi.year)
print(simdi.hour)
print(simdi.minute)
print(simdi.second)


print('ctime')
result = datetime.ctime(simdi)
print(result)



print('strftime')
result = datetime.strftime(simdi,'%Y')
print(result)
result = datetime.strftime(simdi,'%X')
print(result)
result = datetime.strftime(simdi,'%d')
print(result)
result = datetime.strftime(simdi,'%A')
print(result)
result = datetime.strftime(simdi,'%B')
print(result)
result = datetime.strftime(simdi,'%Y %B %A')
print(result)



t = '21 Nisan 2019'
gun, ay, yil = t.split()
print(gun)
print(ay)
print(yil)


t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(dt)
print(dt.year)
print(dt.day)


birthday = datetime(1986,3,16,12,30,)
print(birthday)


result = datetime.timestamp(birthday)  #saniye
print(result)

result = datetime.fromtimestamp(result) #saniye to datetime
print(result)

result = datetime.fromtimestamp(0)
print(result)


result = simdi - birthday   #timedelta
print(result)

# result = result.days
# print(result)


result = result.seconds
print(result)


result = simdi + timedelta(days=10,minutes=50)
print(result)


result = simdi - timedelta(days=20)
print(result)