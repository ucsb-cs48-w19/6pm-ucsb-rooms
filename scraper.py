import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re
import sys


#SCROLL TO THE BOTTOM FOR TIPS ON USING THE SCRAPER
#SEE COMMENTS AT THE BOTTOM

class Time:
        
        #A Class Time has a starting time and an ending time (string, i.e. "12:50pm")
        #Belongs to a Day
        def __init__(self, start, end):
                self.start=start
                self.end=end
        def setStart(self, start):
            self.start=start
        def setEnd(self, end):
            self.end=end    
        def getStart(self):
                return self.start
        def getEnd(self):
                return self.end
        def toString(self):
            return ":" + self.start + "-" + self.end + ":"

        def timeStoi(self, input):
            string=input.split(":")[0]+input.split(":")[1][0:2]
            number=int(string)
            if "pm" in input:
                number=number+1200
            return number  
        
        def getStartInt(self):
                return self.timeStoi(self.start)
        def getEndInt(self):
                return self.timeStoi(self.end)
              
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
            
            
    
    def addTime(self,t):
        start=t.split(" - ")[0]
        end=t.split(" - ")[1]
        
        #avoid null pointer when checking for repeats
        if not self.times:
            self.times.append(Time(start, end))
         #no repeats   
        elif any(start!=time.getStart() for time in self.times):
            self.times.append(Time(start, end))

    def printClassDay(self):
        for time in self.times:
            print(time.getStart(), " - ", time.getEnd())
        
class Room:
    
    #A class Room has a list of days
    #Belongs to a Building
    def __init__(self, number):
        self.number=number
        self.times= {}
        
    def setNumber(self, number):
            self.number=number   
    
    def getNumber(self):
            return self.number
            
    def setDays(self, times):
            self.times=times 
            
    def getDays(self):
                return self.times  
        
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
            
    def getRoomNumbers(self):
        return self.rooms.keys()
        
    def getSpecificRoom(self, number):
        return self.rooms.get(number)
    
    def addToRoom(self, number, days, times):
        if (number not in self.rooms):
            self.rooms[number] =Room(number)
            
        self.rooms.get(number).addTimesDays(days, times)
    


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
    
    def getRooms(self, building):
        b=self.buildings.get(building)
        return b.rooms
        
    
    def getDays(self, building, room):
        return self.buildings.get(building).getRooms().get(room).getDays()
    
    def getTimes(self, building, room, day):
        return self.getBuildings().get(building).getRooms().get(room).getDays().get(day).getTimes()    
    
    def iterateAnthropology(self):

        si = Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        print("\nNOTE: Takes about 1 minunte to scrape Anthropology list of data")

        num =len(si.options)

        s1=Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        s1.select_by_index(0)
        self.driver.find_element_by_name("ctl00$pageContent$searchButton").click()

        self.readSubjectInfo()  #Commented out for testing purposes
        self.driver.close()    
    
      
    def iterateSubjects(self):

        si = Select(self.driver.find_element_by_id("ctl00_pageContent_courseList"))
        print("\nNOTE: Takes about 10-15 mins to scrape full list of data") 

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
            
            
            if (building!="invalid")  :
                if (building not in self.buildings):
                    self.buildings[building] =Building(building)
                self.buildings.get(building).addToRoom(room, days, times) 
                
                
                
            
    def print_class_day(self, building, room, day):
        self.buildings.get(building).getRooms().get(room).getDays().get(day[0]).printClassDay()
            
    def parse_room_building(self, building_number):
        
        
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

#        
scrape=Scraper()
scrape.iterateAnthropology()

for building in scrape.getBuildings():
    print("\n",building)
    for room in scrape.getRooms(building):
        print(room)
        for day in scrape.getDays(building, room):
            print(day)
            for time in scrape.getTimes(building, room, day):
                print(time.getStart(), " - ", time.getEnd())  
                print(time.getStartInt(), " - ", time.getEndInt())
    
    

