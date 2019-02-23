from app import db
import time
from math import floor


class Building(db.Model):
    __tablename__ = "building"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)

    rooms = db.relationship('Room', backref='owning_building', lazy=True)

    def __repr__(self):
        return "<Building: {}>".format(self.name)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            }


class Room(db.Model):
    """"""
    __tablename__ = "room"

    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String, nullable=False)
    room_type = db.Column(db.String)

    days = db.relationship('Day', backref='owning_room')

    building_id = db.Column(db.Integer, db.ForeignKey("building.id"), nullable=False)

    # Note, 1440 is the maximum number of minutes any room can be free, because it's 24*60.
    minutes_free = 1440
    
    time_room_free = "Free All Day"

#    building = db.relationship("Building", backref=db.backref(
#        "room", order_by=id), lazy=True)

    def __lt__(self, other):
        return other.minutes_free < self.minutes_free

    def time_in_minutes(self, input):
        print(input)
        string = input.split(":")[0] + input.split(":")[1][0:2]
        number = int(string)
        if "PM" in input and number < 1200:
            number = number + 1200
        elif number >= 1200 and number <= 1259:
            number - 1200
        number = (number // 100) * 60 + int(string[1:])
        return number

    def free_time(self, day, time):
        time = self.time_in_minutes(time)
        print("Day is:", day, "Time is:", time, "Room is:", self.roomnumber)
 #         print(self.days)
        today = 0
#         today = self.days[0]
        for d in self.days:
            if d.name == day:
                today = d 
#                 print("found the da:", d.name)
 #         print("Today is now:", today)
        if today == 0:
            return "Free All Day"
        else:
            times = today.ranges.split("##")
            for class_time in times:
                class_time = class_time.replace("#", "")
  
                t = class_time.split('-')
                start = self.time_in_minutes(t[0])
                end = self.time_in_minutes(t[1])
                print("number is:", time, start)
                if time < start:
#                     start_minutes = (start // 100) * 60
#                     time_minutes = (time // 100) * 60
                    minutes_free = (start - time) % 60
                    hours_free = (start - time) // 60

                    self.minutes_free = start - time
                    self.time_room_free = "Free for: " + str(hours_free) + " hrs " + str(minutes_free) + " mins"
                    return self.time_room_free
                elif time < end:
                    minutes_free = (end - time) % 60
                    hours_free = (end - time) // 60
                    self.minutes_free = -(start - time)
                    self.time_room_free = "Not free for: " + str(hours_free) + " hrs " + str(minutes_free) + " mins"
                    return self.time_room_free
        return "Free All Day"

    def __repr__(self):
        return "Room is: {}, Building is: {}".format(self.roomnumber, self.owning_building.name)

    def __init__(self, roomnumber, room_type, building_id):
        self.roomnumber = roomnumber
        self.room_type = room_type
        self.building_id = building_id

    def serialize(self):
        return {
            'id': self.id,
            'roomnumber': self.roomnumber,
            'room_type': self.room_type
            }


class Day(db.Model):
    __tablename__ = "day"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ranges = db.Column(db.String)

    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)

    def add_time(self, time):
        self.ranges = self.ranges + time

    def __repr__(self):
        # return "Day is: {}, Time ranges are: {}, Owning room is: {}".format(self.name, self.ranges, self.owning_room.roomnumber)
        return "On: {} Time ranges are: {}".format(self.name, self.ranges)

    def __init__(self, name, ranges, room_id):
        self.name = name
        self.ranges = ranges
        self.room_id = room_id
