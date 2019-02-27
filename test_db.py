import os
import tempfile
import pytest
from app import db
from models import Building, Room, Day


def test_database0():

	assert Building.__tablename__ == "building"

def test_database1():

	assert Room.__tablename__ == "room"

def test_database2():

	assert Day.__tablename__ == "day"

def test_time_in_minutes():
	rm0 = Room(3515, 1)
	assert rm0.time_in_minutes("12:03PM") == 723
	

def test_time_in_minutes1():
	rm1 = Room(1503, 2)
	assert rm1.time_in_minutes("1:17AM") == 77

	
def test_time_in_minutes2():
	rm2 = Room(2010, 3)
	assert rm2.time_in_minutes("4:03PM") == 963
	

def test_time_in_minutes3():
	rm3 = Room(1234, 4)
	assert rm3.time_in_minutes("8:30AM") == 510

def test_free_time():
	rm4 = Room(2345, 5)
	assert rm4.free_time(0, "3:20pm") == "Free Rest of Day"
	
def test_add_time():
	Bd0 = Building("HSSM")
	assert bd0.id == 1

def test_add_time():
	bd1 = Building("LSB")
	assert bd1.__init__("LSB") == "LSB"


	
