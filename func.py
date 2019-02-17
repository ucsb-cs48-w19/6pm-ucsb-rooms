#parse and turn into int obj
#store
import re
import copy

#set this =  data from result.html (the time ranges) and move it inside the parseAndStore function
str0 =": :4:00pm-4:50pm::11:00am-12:15pm::5:00pm-5:50pm::1:00pm-1:50pm::2:00pm-3:15pm:"

def parse(str0):
    str1 = str0.replace("-","::")
    str1 = str1.replace(" ","")
    time = str1.split("::")

    objList = [];
    available = [];

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

    availableStart = objList[1::2]
    availableStart.append(700)
    availableEnd = objList[::2]
    availableEnd.append(2359)
    availableStart.sort()
    availableEnd.sort()
    print(availableStart)
    print(availableEnd)

    i = 0
    while i < len(availableStart):
        startTime = availableStart[i]
        startTime =str(startTime)
        endTime = availableEnd[i]
        endTime = str(endTime)
        output = "Available from: " + startTime + " to " + endTime
        available.append(output)
        i += 1

    print(available)

parse(str0)
