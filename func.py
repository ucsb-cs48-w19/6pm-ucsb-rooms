#parse and turn into int obj
#store
#simple ideas on how to turn data from result.html into useful form
from datetime import datetime
from pytz import timezone
import pytz
import re
import copy


#set this =  data from result.html (the time ranges) and move it inside the parseAndStore function
#following is a sample result (str0)
str0 =": :4:00pm-4:50pm::11:00am-12:15pm::5:00pm-5:50pm::1:00pm-1:50pm::2:00pm-3:15pm:"

###current time####
date_format='%H%M'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific'))
intTime = int(date.strftime(date_format))
print (intTime)

#########################

def parse(str0):
    str1 = str0.replace("-","::")
    str1 = str1.replace(" ","")
    time = str1.split("::")

    objList = [];   #list hold all unavailable times
    available = [];  #list hold pair of available times  ex: available from 700-1100 (in strings)
    availableList = []; #list hold all available time from 700-2359 (as integers)

    for range in time:
        range = range.replace(":","")

        if "am" in range:
            range = range.replace("am","")
            range = int(range)
            objList.append(range)
        elif "pm" in range:
            range = range.replace("pm","")
            range = int(range)
            if range >= 1200 and range < 1259:
                objList.append(range)
            else:                               #convert to military time and string into int
                range += 1200
                objList.append(range)



    objList.sort()
    print(objList)      # now objList has all the unavailable time
# everything is store in a list at an int
# hardcoded 7am to 1159pm for available time ranges

    availableStart = objList[1::2]
    availableStart.append(700)
    availableEnd = objList[::2]
    availableEnd.append(2359)
    availableStart.sort()
    availableEnd.sort()
    print(availableStart)   # list with available start time
    print(availableEnd)    # list with available end time

    i = 0
    while i < len(availableStart):
        startTime = availableStart[i]
        startTime =str(startTime)
        intStartTime = int(startTime)
        availableList.append(intStartTime)

        endTime = availableEnd[i]
        endTime = str(endTime)
        intEndTime = int(endTime)
        availableList.append(intEndTime)

        output = "Available from: " + startTime + " to " + endTime
        available.append(output)
        i += 1

    print(available)
    print("........................")
    print(availableList)

    #######if available implementation########
    #availableList is a combination of startTime list and Endtime objList
    # room is available if current time is in between start and end time

    j = 0
    TimeOfAvailability = 0
    ifavailable = "not available at this moment"
    while j < len(availableList):
        if(intTime >= availableList[j] and intTime < availableList[j+1]):
            ifavailable = "available at this moment"
            break
            print(ifavailable)
        j += 2

    print(ifavailable)


parse(str0)
