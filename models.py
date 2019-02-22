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

#    building = db.relationship("Building", backref=db.backref(
#        "room", order_by=id), lazy=True)

    def time_stoi(self, input):
        string = input.split(":")[0] + input.split(":")[1][0:2]
        number = int(string)
        if "pm" in input and number < 1200:
            number = number + 1200
        elif number >= 1200 and number <= 1259:
            number - 1200
        return number

    def free_time(self, day, time):
        time = self.time_stoi(time)
 #         print("Day is:",day,"Time is:",time)
 #         print(self.days)
        today = 0
#         today = self.days[0]
        for d in self.days:
            if d.name == day:
                today = d 
 #                print("found the da:", d.name)
 #         print("Today is now:", today)
        if today == 0:
             return "Free All Day"
        else:
            times = today.ranges.split("##")
            for class_time in times:
                class_time = class_time.replace("#", "")
  
                t = class_time.split('-')
                start = self.time_stoi(t[0])
 #                 end = self.time_stoi(t[1])
 #                 print("number is:", start, end)
                  
                if time < start:
 #                     print("Free time is:", start - time)
                    free_hours = floor((start - time) / 100)
                    free_mins = ((start - time) * 0.6) % 60 
                    return str(free_hours) + " hrs " + str(free_mins) + " mins"
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
