import pytest
from currentTimeObj import getAvailableTime

def getAvailableTime_0():
  assert getAvailableTime(150, 520) == pytest.approx(210)

def getAvailableTime_1():
  assert getAvailableTime(250, 520) == pytest.approx(150)

def getAvailableTime_2():
  assert getAvailableTime(350, 520) == pytest.approx(90)

def getAvailableTime_3():
  assert getAvailableTime(450, 520) == pytest.approx(30)
  
def getAvailableTime_4():
  assert getAvailableTime(519, 520) == pytest.approx(1)
