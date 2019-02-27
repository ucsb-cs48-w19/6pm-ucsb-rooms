import pytest
from currentTimeObj import getAvailableTime

def test_getAvailableTime_0():
  assert getAvailableTime(150, 520) == pytest.approx(210)

def test_getAvailableTime_1():
  assert getAvailableTime(250, 520) == pytest.approx(150)

def test_getAvailableTime_2():
  assert getAvailableTime(350, 520) == pytest.approx(90)

def test_getAvailableTime_3():
  assert getAvailableTime(450, 520) == pytest.approx(30)
  
def test_getAvailableTime_4():
  assert getAvailableTime(519, 520) == pytest.approx(1)
