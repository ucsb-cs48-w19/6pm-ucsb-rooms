import pytest
from currentTimeObj import getAvailableTime

def getAvailableTime_0(150, 520):
  assert getAvailableTime() == 210

def getAvailableTime_0(250, 520):
  assert getAvailableTime() == 150

def getAvailableTime_0(350, 520):
  assert getAvailableTime() == 90

def getAvailableTime_0(450, 520):
  assert getAvailableTime() == 30
  
def getAvailableTime_0(519, 520):
  assert getAvailableTime() == 1
