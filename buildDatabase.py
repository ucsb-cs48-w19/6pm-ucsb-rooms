import scraper
from scraper import Scraper
from app import db
from models import Building, Room

scrape=Scraper()
scrape.iterateAnthropology()
print("====THE SCRAPER FINISHED RUNNING, NOW WE'RE GONNA VIEW THE OBJECT STORED RESULTS=====")
for building in scrape.getBuildings():    
    for room in scrape.getBuildings().get(building).getRooms():
        for day in scrape.getBuildings().get(building).getRooms().get(room).getTimes():
            print("Today's schedule for ", building,room, day)
            scrape.print_class_day(building, room, day)  