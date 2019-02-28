import datetime
import pytest
from app import get_time_pst, get_day_pst

now = datetime.datetime.now()
Time = now.time()
Test_Time = Time.strftime('%I:%M%p').lstrip('0')
weekday = now.strftime("%A")
weekdayLetter = weekday[0]

#print(weekday)
#print(Test_Time)
def test_get_time_pst():
    assert get_time_pst() == Test_Time

def test_get_day_pst():
    if(weekday == 'Thursday'):
        assert get_day_pst() == 'R'
    else:
        assert get_day_pst() == weekdayLetter
