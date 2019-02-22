from datetime import datetime
from pytz import timezone
import pytz

date_format='%H%M'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific')) # get TimeZone for SB
intTime = int(date.strftime(date_format))
print ("current time as int: ", intTime)
################## int Time obj for current time###########################


####break down intTime for comparison purpose######
hours = intTime // 100
minutes = intTime % 100
TotalTimeInMinutes = (hours * 60) + minutes
print("hours:",hours)
print("minutes:",minutes)
print("sum of time in minutes:",TotalTimeInMinutes, " minutes")

#####example for available time in mins######
# let time A = current Time
# let time S = StartTime(look at func.py  the while loop for if available)
# let time E = Endtime(look at func.py)
# let time A >= S and A < E

timeA = 150   # 0150 or 1:50am
timeE = 520   # 0520 or 5:20am

# let say i search for room at time 1:50am
# and the room is available from 1:00am to 5:20am
# i can obtain the remaining available time of the room doinf this........
TotalTimeA = ((timeA // 100) * 60) + (timeA % 100)
TotalTimeE = ((timeE // 100) * 60) + (timeE % 100)
availableTimeInMins = TotalTimeE - TotalTimeA

print("you have", availableTimeInMins, "minutes available for this room")

remainHours = availableTimeInMins // 60
remainMinutes = availableTimeInMins % 60

print("you have",remainHours,"hour/s",remainMinutes, "minutes left for this room")
