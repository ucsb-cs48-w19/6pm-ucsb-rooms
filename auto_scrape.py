from apscheduler.schedulers.blocking import BlockingScheduler
import scraper
from scraper import Scraper
from app import db
from models import Building, Room, Day
from astropy.units import day

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('interval', minutes=3)
def scheduled_job():
    scrape=Scraper()

    #scrape.iterateSubjects()
    scrape.iterateAnthropology()

    print("====THE SCRAPER FINISHED RUNNING, NOW WE'RE GONNA VIEW THE OBJECT STORED RESULTS=====")

    for building in scrape.getBuildingsOrdered():
        name = building.getName().rstrip()
        if (len(Building.query.filter_by(name=name).all()) == 0):
            print("Adding:", building.name)
            b = Building(name=name)
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

sched.start()
