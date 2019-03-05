import scraper
from scraper import Scraper
from app import db
from models import Building, Room, Day
from astropy.units import day

#db.create_all()

scrape=Scraper()

scrape.iterateSubjects()
#scrape.iterateAnthropology()

print("====THE SCRAPER FINISHED RUNNING, NOW WE'RE GONNA VIEW THE OBJECT STORED RESULTS=====")

def get_pretty_name(abbrev):
    if (abbrev=="387"):
        return "Modular Classrooms"
    elif (abbrev=="434"):
        return "Former Women's Center"
    elif (abbrev=="451"):
        return "Military Science Building"
    elif (abbrev=="942"):
        return "Building 942"
    elif (abbrev=="ARTS"):
        return "Arts & University Art Museum"
    elif (abbrev=="BIOEN"):
        return "Bioengineering Building"
    elif (abbrev=="BRDA"):
        return "Broida Hall"
    elif (abbrev=="BREN"):
        return "Bren Hall"
    elif (abbrev=="BSIF"):
        return "Biological Sciences Instructional Facility"
    elif (abbrev=="BUCHN"):
        return "Buchanan Hall"
    elif (abbrev=="CAMPBHALL"):
        return "Campbell Hall"
    elif (abbrev=="CHEM"):
        return "Chemistry Building"
    elif (abbrev=="CRST"):
        return "477"
    elif (abbrev=="ED"):
        return "Education Building"
    elif (abbrev=="ELLSN"):
        return "Ellison Hall"
    elif (abbrev=="ELNGS"):
        return "Elings Hall"
    elif (abbrev=="EMBARHALL"):
        return "Embarcadero Hall"
    elif (abbrev=="ESB"):
        return "Engineering Sciences Building"
    elif (abbrev=="GIRV"):
        return "Girvetz Hall"
    elif (abbrev=="HARDR" or abbrev=="HARDRSTADM"):
        return "Harder Stadium"
    elif (abbrev=="HSSB"):
        return "Humanities and Social Sciences Building"
    elif (abbrev=="HFH"):
        return "Harold Frank Hall"
    elif (abbrev=="ICA"):
        return "Intercollegiate Building"
    elif (abbrev=="KERR"):
        return "Kerr Hall"
    elif (abbrev=="LIB"):
        return "Library"
    elif (abbrev=="LSB"):
        return "Life Science Building"
    elif (abbrev=="MLAB"):
        return "Marine Biology Laboratory"
    elif (abbrev=="MUSIC"):
        return "Music Laboratory"
    elif (abbrev=="MUSICLLCH"):
        return "Lotte Lehmann Concert Hall"
    elif (abbrev=="NH"):
        return "North Hall"
    elif (abbrev=="NOBLE"):
        return "Noble Hall"
    elif (abbrev=="PHELP"):
        return "Phelps Hall"
    elif (abbrev=="PLLOKTHTR"):
        return "Pollock Theater"
    elif (abbrev=="PSYCH"):
        return "Psychology Building"
    elif (abbrev=="SH"):
        return "South Hall"
    elif (abbrev=="SRB"):
        return "Student Resources Building"
    elif (abbrev=="SSMS"):
        return "Social Sciences and Media Studies"
    elif (abbrev=="TD-E"):
        return "Theater/Dance East"
    elif (abbrev=="TD-W"):
        return "Theater/Dance West"
    elif (abbrev=="WEBB"):
        return "Webb Hall/Geological Sciences Building"
    else:
        return abbrev

for building in scrape.getBuildingsOrdered():
    name = building.getName().rstrip()
    if (len(Building.query.filter_by(name=name).all()) == 0):
        print("Adding:", building.name)
        b = Building(name=name, full_name=get_pretty_name(name).strip())
        db.session.add(b)

db.session.commit()

for building in scrape.getBuildingsOrdered():
    b = Building.query.filter_by(name=building.getName().rstrip()).first()
    for room in building.getRooms2():

        if (not (room in b.rooms)):
                print("Adding:", room.number)
                r1 = Room(roomnumber=room.number.rstrip(), building_id=b.id)
                db.session.add(r1)

db.session.commit()

for building in scrape.getBuildingsOrdered():
    b = Building.query.filter_by(name=building.name.rstrip()).first()

    for room in building.getRooms2():

        r_id = 0
        for r in b.rooms:
            if (r.roomnumber == room.number):
                r_id = r.id
                break

        for day in room.getDays2():
            day.sortTime()
            times = day.timeString()
            #times.sort()
            d = Day(name=day.day, ranges="",room_id=r_id)
            print("Adding day:",day.day)
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
