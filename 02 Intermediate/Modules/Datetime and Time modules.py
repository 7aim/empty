import datetime
import time

#datetime

today = datetime.date.today()
mybirth = datetime.date(2007,5,6)
mybirth.year

daytime = mybirth-today
print(daytime)
print(daytime.days)

tomorrow = mybirth - datetime.timedelta(days=81)
print(tomorrow)

timee = datetime.time(22,44)
print(timee)
print(timee.hour)

dt = datetime.datetime(2025,2,13,19,11,56)
print(dt)

#time

while True:
    zaman = time.localtime() #shows present time (readable)
    x = zaman[3]
    y = zaman[4]
    z = zaman[5]
    print("Saat: {}:{}:{}".format(x,y,z))
    time.sleep(1)

start = time.time() #shows present time (not readable)
time.sleep(10)
finish = time.time()
print(finish-start)

#year, month, day = map(int, date_str.split(','))  #convert string parts to integer
