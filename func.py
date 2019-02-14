#parse and turn into int obj
#store
import re
import copy

str =": :4:00pm-4:50pm::11:00am-12:15pm::5:00pm-5:50pm::1:00pm-1:50pm::2:00pm-3:15pm:"
str1 = str.replace("-","::")

time = str1.split("::")

objList = [];

for range in time:
    range = range.replace(":","")
    range = range.replace(" ","")
    if "am" in range:
        range = range.replace("am","")
        range = int(range)
    elif "pm" in range:
        range = range.replace("pm","")
        range = int(range)
        range += 1200
    objList.append(range)

print(objList)

# everything is store in a list at an int
#just turn this into class and change the str = data from db
#123
