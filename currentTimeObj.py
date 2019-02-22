from datetime import datetime
from pytz import timezone
import pytz

date_format='%H%M'
date = datetime.now(tz=pytz.utc)
date = date.astimezone(timezone('US/Pacific'))
intTime = int(date.strftime(date_format))
print (intTime)
################## int Time obj for current time###########################
