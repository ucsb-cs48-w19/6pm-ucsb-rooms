#parse and turn into int obj
#store
import re
import copy

#set this =  data from result.html (the time ranges) and move it inside the parseAndStore function
str =": :4:00pm-4:50pm::11:00am-12:15pm::5:00pm-5:50pm::1:00pm-1:50pm::2:00pm-3:15pm:"

def parse(str):
    str1 = str.replace("-","::")
    str1 = str1.replace(" ","")
    time = str1.split("::")

    objList = [];

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

    print(objList)      # now objList has all time
# everything is store in a list at an int

#parse(str)

def ifAvailable(int1, int2):
    #take systime , turn it into 4 digit int
    #go thru the list, compare systime with with item 1&2, 3&4, 5&6.....
    # ex: int1 = item 1, int2 = item 2 , if systime >= int1 and <= int2
    #return unavailable
    #else return available

    def availableTime(int2, int3):
    #same concept with 2 special case 700 to item1 and last item to 2300
    #return item int2 - int1 = available time
