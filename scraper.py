import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re
import sys
from datetime import datetime

#SCROLL TO THE BOTTOM FOR TIPS ON USING THE SCRAPER
#SEE COMMENTS AT THE BOTTOM
class Day:
    
    #A class room Day has a list of class times.
    #Belongs to a Room
    def __init__(self, day):
        self.day=day
        self.times=[]
        
    
    def setDay(self, day):
            self.day=day
    
    def setTimes(self, times):
            self.times=times   
    
    def getDay(self):
                return self.day
    def getTimes(self):
                return self.times

    """
    New Methods added: converting times to string, adding times as list
    of ints, sorting times as ints
    """
    def pairwise(self, iteratable):
        a = iter(iteratable)
        return zip(a, a)
    # Method to remove the
    def timeString(self):
        s = ""
        for x, y in self.pairwise(self.times):
            s += "#" + datetime.strptime(str(x), '%H%M').strftime('%I:%M%p').lstrip("0") + "-" + datetime.strptime(str(y), '%H%M').strftime('%I:%M%p').lstrip("0") + "#"
        return s

    # Method to add time as list of ints
    def addTime(self, t):
        t = t.replace(" ", "")
        split = re.split(r"-", t)
        firstTime = int(datetime.strptime(str(split[0]), '%I:%M%p').strftime('%H%M'))
        secondTime = int(datetime.strptime(str(split[1]), '%I:%M%p').strftime('%H%M'))
        self.times.append(firstTime)
        self.times.append(secondTime)
    #Method to sort list of ints and remove duplicates
    def sortTime(self):
        self.times = list(set(self.times))
        self.times.sort()


class Room:
    
    #A class Room has a list of days
    #Belongs to a Building
    def __init__(self, number):
        self.number=number
        self.times= {}
        
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.number == other.number
        
        
    def __lt__(self, other):
        return self.number < other.number
        
    def setNumber(self, number):
            self.number=number   
    
    def getNumber(self):
            return self.number
            
    def setDays(self, times):
            self.times=times 
            
    def getDays(self):
                return self.times  
            
    def getDays2(self):
                return self.times.values()  
        
    def addTimesDays(self, days, time):
        days= days.replace(" ", "")
        for day in days:
            if (day not in self.times):
                self.times[day]= Day(day)
                
            self.times.get(day).addTime(time)
            
class Building:
    
    #A Building has a list of rooms.
    def __init__(self, name):
        self.name=name
        self.rooms={}
        
        
    def setName(self, name):
            self.name=name   
    
    def getName(self):
                return self.name
            
    def setRooms(self, rooms):
            self.rooms=rooms 
            
    def getRooms(self):
                return self.rooms
            
    def getRooms2(self):
                roomsOrdered=list(self.rooms.values())
                roomsOrdered.sort()
                return roomsOrdered
            
    def getRoomNumbers(self):
        return self.rooms.keys()
        
    def getSpecificRoom(self, number):
        return self.rooms.get(number)
    
    def addToRoom(self, number, days, times):
        if (number not in self.rooms):
            self.rooms[number] =Room(number)
            
        self.rooms.get(number).addTimesDays(days, times)
        
    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name
        
        
    def __lt__(self, other):
        return self.name < other.name
    


class Scraper(object):
    
    def __init__(self):
        self.options = Options() 
        self.options.add_argument("--headless")  #Commented out for testing purposes
        #self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),   options=self.options)
        platform = sys.platform
        
        if (platform == "linux"):
            self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_linux'),   options=self.options)
        else:
            self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver_mac'),   options=self.options)
        self.driver.get("https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx")
        assert "Curriculum Search" in self.driver.title
        self.buildings={}
        
        
        
    
    
            
    #chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'    
    
    def getBuildings(self):
        return self.buildings
    
    def getBuildingsOrdered(self):
        orderedBuildings=list(self.buildings.values())
        orderedBuildings.sort()
        return orderedBuildings
    
    def getRooms(self, building):
        b=self.buildings.get(building)
        return b.rooms
        
    
    def getDays(self, building, room):
        return self.buildings.get(building).getRooms().get(room).getDays()
    
    def getTimes(self, building, room, day):
        return self.getBuildings().get(building).getRooms().get(room).getDays().get(day).getTimes()    
    
    def iterateAnthropology(self):

        si = Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        print("\nNOTE: Takes about 1 minute to scrape Anthropology list of data")
        sg = Select(self.driver.find_element_by_id("ctl00_pageContent_dropDownCourseLevels"))
        sg.select_by_index(2)
        num =len(si.options)

        s1=Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        s1.select_by_index(0)
        self.driver.find_element_by_name("ctl00$pageContent$searchButton").click()

        self.readSubjectInfo()  #Commented out for testing purposes
        self.driver.close()    
    
      
    def iterateSubjects(self):

        si = Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        print("\nNOTE: Takes about 10-15 mins to scrape full list of data") 
        sg = Select(self.driver.find_element_by_id("ctl00_pageContent_dropDownCourseLevels"))
        sg.select_by_index(2)
        num =len(si.options)
        
        for index in range(0, num):
            s1=Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
            s1.select_by_index(index)
            self.driver.find_element_by_name("ctl00$pageContent$searchButton").click()
            
            self.readSubjectInfo()  #Commented out for testing purposes
        self.driver.close()
    
    
    
    
  
    def readSubjectInfo(self):
        
        rowCount= len(self.driver.find_elements_by_xpath("//*[@class='gridview']/tbody/tr"))
        
        for index in range(1, rowCount):
            #days already parsed correctly
            days = self.driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[7]").text
               
            #times will be parsed in the Day Class under the addTime method
            times = self.driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[8]").text
               
            #Need to parse Building from Room number
            building_number = self.driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[9]").text
               
            #print("\n",building_number, days, times)
            building, room=self.parse_room_building(building_number) 
            status = self.driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[4]").text

            if (building!="invalid" and status.strip()!="Cancelled"):
                if (building not in self.buildings):
                   self.buildings[building] =Building(building.strip())
                self.buildings.get(building).addToRoom(room.strip(), days, times) 
                
                
            
    def print_class_day(self, building, room, day):
        self.buildings.get(building).getRooms().get(room).getDays().get(day[0]).printClassDay()
            
    def parse_room_building(self, building_number):
        building = ""
        room = ""
        invalid = ["NO", "PLLOKSTG", "MUSICGHALL", "HARDRSTADM", "RGYM", "TRACKFIELD", "ENGR", "TBA", "T B A", "ON LINE", "ONLINE", "IV", "BSBL", "RECEN", "SB HARBR", "ZODO", "REGYM", "EVENTCENTR", "GOLF", "STORKFIELD", "SWIM", "SFTBLFIELD"]
        if any(word in building_number for word in invalid):
            return "invalid", "invalid"
        if " " in building_number:
            split = building_number.split(" ")
            building = split[0]
            room = split[1]
        else:
            split = re.findall(r"[^\W\d_]+|\d+", building_number)
            if len(split) > 2:
                split[1] = split[1] + split[2]
            elif len(split) == 1:
                building = split[0]
                room = "N/A"
            elif len(split) == 2:
                building = split[0]
                room = split[1]
            else:
                building = "invalid"
                room = "invalid"
        return building, room
    
    def parse_room_building2(self, building_number):
        
        invalid_list=["ONLINE", "ON LINE", "T B A","NO ROOM", "TBA" ,""]
        
        if building_number in invalid_list:
                return "invalid", "invalid"
        m= len(building_number)
        
        if (re.search(" ", building_number)):
            if not re.search(" \d", building_number):
                m= len(building_number)
            else: 
                m = re.search(" \d", building_number).start()
        else:
            if not re.search("\d", building_number):
                m= len(building_number)
            else: 
                m = re.search("\d", building_number).start()
            
        building=building_number[ 0 : m ] 
        room=building_number[m:len(building_number)]
        
        return building, room
            
            
#To Use Scraper, 
#   create a scraper object and build the the temporary list of data  
#   (This takes about 15 mins to run)
#   i.e.
   
#scrape=Scraper()
#scrape.iterateAnthropology()

#for building in scrape.getBuildingsOrdered():
 #   print("\n",building.getName())
  #  for room in building.getRooms2():
   #     print(room.getNumber())
    #    for day in room.getDays2():
     #       print(day.getDay())
      #      print(day.timeString())
    
    
