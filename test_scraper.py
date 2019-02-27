import pytest

import pytest
import scraper
from scraper import Scraper
from scraper import Building
from scraper import Room
from scraper import Day


def test_parse_room_building0():
    invalid_list=["ONLINE", "ON LINE", "T B A","NO ROOM", "TBA" ,""]#TO DO: replace with full invalid list
    for invalid in invalid_list:
        assert "invalid", "invalid" == parse_room_building(invalid)
def test_parse_room_building1():
    assert "HSSB", "1713" == parse_room_building("HSSB 1713")

def test_parse_room_building2():
    assert "PHELP", "3526" == parse_room_building("PHELP3526")

def test_parse_room_building3():
    assert "EMBARHALL", "" == parse_room_building("EMBARHALL")



def test_parse_room_building0():    
    invalid_list=["ONLINE", "ON LINE", "T B A","NO ROOM", "TBA" ,""]#TO DO: replace with full invalid list
    for invalid in invalid_list:
        assert "invalid", "invalid" == parse_room_building(invalid)
        
def test_parse_room_building1():
    assert "HSSB", "1713" == parse_room_building("HSSB 1713")
    
def test_parse_room_building2():
    assert "PHELP", "3526" == parse_room_building("PHELP3526")
    
def test_parse_room_building3():
    assert "EMBARHALL", "" == parse_room_building("EMBARHALL")
    
