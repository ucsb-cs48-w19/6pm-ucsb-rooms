import scraper
from scraper import Scraper
from app import db
from models import Building, Room

#db.create_all()

scrape=Scraper()
scrape.iterateAnthropology()
print("====THE SCRAPER FINISHED RUNNING, NOW WE'RE GONNA VIEW THE OBJECT STORED RESULTS=====")

for building in scrape.getBuildings():
    
    building = scrape.getBuildings().get(building)
    if (len(Building.query.filter_by(name=building.getName()).all()) == 0):
        print("Adding:", building.name)
        b = Building(name=building.name.rstrip())
        db.session.add(b)

db.session.commit()

for building in scrape.getBuildings(): 
    building_object = scrape.getBuildings().get(building)
    b = Building.query.filter_by(name=building_object.name).first()
    for room in building_object.getRooms():
        room = scrape.getBuildings().get(building).getRooms().get(room)
        if (not (room in b.rooms)):
                print("Adding:", room.number)
                r1 = Room(roomnumber=room.number.rstrip(),room_type='trashy_room_standard', building_id=b.id)
                db.session.add(r1)

db.session.commit()            

# for building in scrape.getBuildings():    
#     for room in scrape.getBuildings().get(building).getRooms():
#         for day in scrape.getBuildings().get(building).getRooms().get(room).getTimes():
#             print("Today's schedule for ", building,room, day)
#             scrape.print_class_day(building, room, day)  