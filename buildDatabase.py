import scraper
from scraper import Scraper
from app import db
from models import Building, Room, Day
from astropy.units import day

#db.create_all()

scrape=Scraper()

#scrape.iterateSubjects()
scrape.iterateAnthropology()

print("====THE SCRAPER FINISHED RUNNING, NOW WE'RE GONNA VIEW THE OBJECT STORED RESULTS=====")

for building in scrape.getBuildings():
    name = building.rstrip()
    building = scrape.getBuildings().get(building)
    if (len(Building.query.filter_by(name=name).all()) == 0):
        print("Adding:", building.name)
        b = Building(name=name)
        db.session.add(b)

db.session.commit()

for building in scrape.getBuildings():
    building_object = scrape.getBuildings().get(building)
    b = Building.query.filter_by(name=building_object.getName().rstrip()).first()
    for room in building_object.getRooms():

        room = scrape.getBuildings().get(building).getRooms().get(room)

        if (not (room in b.rooms)):
                print("Adding:", room.number)
                r1 = Room(roomnumber=room.number.rstrip(),room_type='trashy_room_standard', building_id=b.id)
                db.session.add(r1)

db.session.commit()

for building in scrape.getBuildings():
    b = Building.query.filter_by(name=building.rstrip()).first()

    for room in scrape.getBuildings().get(building).getRooms():

        r_id = 0
        for r in b.rooms:
            if (r.roomnumber == room):
                r_id = r.id
                break

        for day in scrape.getBuildings().get(building).getRooms().get(room).getDays():
            scrape.getBuildings().get(building).getRooms().get(room).getDays().get(day).sortTime()
            times = scrape.getBuildings().get(building).getRooms().get(room).getDays().get(day).timeString()
            #times.sort()
            d = Day(name=day,ranges="",room_id=r_id)
            print("Adding day:",day)
            print("Adding times: ", times)
            d.add_time(times)
            db.session.add(d)

db.session.commit()
#             print(timeObject)
#             print(type(timeObject))
#             print(dir(timeObject))
#             print(timeObject[0].toString())

# for building in scrape.getBuildings():
#     for room in scrape.getBuildings().get(building).getRooms():
#         for day in scrape.getBuildings().get(building).getRooms().get(room).getDays():
#             print("Today's schedule for ", building,room, day)
#             scrape.print_class_day(building, room, day)
