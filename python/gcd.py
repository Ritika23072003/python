def gcd(a,b):
    if(b==0):
         return a
    else:
        return gcd(b,a%b)
print(gcd(54,12))
print(gcd(20,15))

print(" ")
#2nd method
def comp(x,y):
    while(y):
        x,y = y,x%y
    return x
print(comp(54,24))
print(" ")

import datetime
#print date and time
print(datetime.datetime)
print(datetime.datetime.now())

#only time
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())

print(" ")
d = datetime.date(2023,5,9)

print(" ")
from datetime import date
today = date.today()
print("current date =",today)

print("")
today = date.today()
print(dir(today))
print("current date =",today.year)
print("current date =",today.month)
print("current date =",today.day)

print(" ")
from datetime import datetime,timedelta
given_date = datetime(2023,5,9)
print(given_date)

day_to_sub = 7
res_date = given_date - timedelta(day_to_sub)
print("New Date")
print(res_date)

#the shiftime() method creates a string from the date time object
from datetime import datetime
now = datetime.now() #current date and time
today = date.today()
year = now.strftime("%Y")
print("year:",year)
month = now.strftime("%m")
print("month:",month)
day = now.strftime("%d")
print("day:",day)
time = now.strftime("%H:%M:%S")
print("time:",time)
date_time = now.strftime("%m/%d/%Y,%H:%M:%S")