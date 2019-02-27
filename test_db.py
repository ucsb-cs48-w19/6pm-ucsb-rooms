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
    rm = Room()

    assert rm.time_in_minutes("12:03PM") == 723
