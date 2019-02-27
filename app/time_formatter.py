import pytz as pz
from datetime import datetime as dt
from pytz import timezone as tz
import calendar

def get_time_pst():
    date = dt.now(tz=pz.utc)
    date = date.astimezone(tz('US/Pacific'))
    return date.strftime('%I:%M%p').lstrip('0')

def get_day_pst():
    date = dt.now(tz=pz.utc)
    date = date.astimezone(tz('US/Pacific'))
    day = calendar.day_name[date.weekday()]

    if (day == "Thursday"):
        day = "R"
    else:
       day = day[0]
    
    return day

