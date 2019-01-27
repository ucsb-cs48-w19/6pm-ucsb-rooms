import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select



class Time:
        start=0
        end=0
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
    day=""
    times=[]

    def __init__(self, day):
        self.day=day
        
    
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
        self.times.append(Time(start, end))
        
class Room:
    times= {}
    number=0
    
    def __init__(self, number):
        self.number=number
        
    def setNumber(self, number):
            self.number=number   
    
    def getNumber(self):
                return self.number
            
    def setTimes(self, times):
            self.times=times 
            
    def getTimes(self):
                return self.times  
            
    def addTimesDays(self, days, time):
        d= days.split()
        for day in d:
            if (day not in self.times):
                self.times[day]= Day(day)
                
            self.times.get(day).addTime(time)
            
class Building:
    rooms={}
    name=""
    
    def __init__(self, name):
        self.name=name
        
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
    



options = Options() 
driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),   options=options)
driver.get("https://my.sa.ucsb.edu/public/curriculum/coursesearch.aspx")
assert "Curriculum Search" in driver.title
        
     
#options.add_argument("--headless")  #Commented out for testing purposes
        
#chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'    


buildings={}

   
def iterateSubjects():
    si = Select(driver.find_element_by_id("ctl00_pageContent_courseList"))
    num =len(si.options)
    for index in range(0, num):
        s1=Select(driver.find_element_by_id("ctl00_pageContent_courseList"))
        s1.select_by_index(index)
        driver.find_element_by_name("ctl00$pageContent$searchButton").click()
        
        readSubjectInfo()  #Commented out for testing purposes
        





def readSubjectInfo():
    
    rowCount= len(driver.find_elements_by_xpath("//*[@class='gridview']/tbody/tr"))
    
    for index in range(1, rowCount):
        #days already parsed correctly
        days = driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[7]").text
        
        #times will be parsed in the Day Class under the addTime method
        times = driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[8]").text
        
        #Need to parse Building from Room number
        builing_number = driver.find_element_by_xpath("//*[@class='gridview']/tbody/tr["+str(index)+"]/td[9]").text
        
        #Parsing to be done here
        
        building=""
        room=""
        
        if (building not in buildings):
            buildings[building] =Building(building)
            
        buildings.get(building).addToRoom(room, days, times)
        
            
        
            
        
        
        
        
        

iterateSubjects()

driver.close()
