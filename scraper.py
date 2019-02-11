import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import re


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
            return "\nClass starts at: " + self.start + " Ends at " + self.end
        
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
            
    def setTimes(self, times):
            self.times=times 
            
    def getTimes(self):
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
        #self.options.add_argument("--headless")  #Commented out for testing purposes
        self.driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),   options=self.options)
        self.driver.get("https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx")
        assert "Curriculum Search" in self.driver.title
        self.buildings={}
        
        
        
    
    
            
    #chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'    
    
    def getBuildings(self):
        return self.buildings    
    
    
    
    
      
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
            
            print("\n",building_number, days, times)
            building, room=self.parse_room_building(building_number)
            
            
            if (building!="invalid")  :
                if (building not in self.buildings):
                    self.buildings[building] =Building(building)
                self.buildings.get(building).addToRoom(room, days, times) 
                
                
                
            
    def print_class_day(self, building, room, day):
        self.buildings.get(building).getRooms().get(room).getTimes().get(day[0]).printClassDay()
            
    def parse_room_building(self, building_number):
        
        
        invalid_list=["ONLINE", "ON LINE", "T B A","NO ROOM", "TBA" ,""]
        
        if building_number in invalid_list:
                return "invalid", "invalid"
        m= len(building_number)
        
        
        if (re.search('[a-zA-Z]', building_number)):
        #If the string contains a letter, i.e. "PHELP1513" or "GIRV 2123",
        #Then split the string at the first index of a digit: 
        #building ="PHELP" room = "1513" 
        #buidling =""
            if not re.search("\d", building_number):
                m= len(building_number)
            else: 
                m = re.search("\d", building_number).start()
            
        else:
            #Otherwise Numerical building, i.e. "387 1015"
            #Split on white space
            m = re.search(" ", building_number).start()
        building=building_number[ 0 : m ] 
        room=building_number[m:len(building_number)]
        return building, room
    
    
    
        
            
            
#To Use Scraper, 
#   create a scraper object and build the the temporary list of data  
#   (This takes about 15 mins to run)
#   i.e.
        
#scrape=Scraper()
#scrape.iterateSubjects()

#for building in scrape.getBuildings():    
#    for room in scrape.getBuildings().get(building).getRooms():
#        for day in scrape.getBuildings().get(building).getRooms().get(room).getTimes():
#            print("Today's schedule for ", building,room, day)
#            scrape.print_class_day(building, room, day)  
  
    
    

