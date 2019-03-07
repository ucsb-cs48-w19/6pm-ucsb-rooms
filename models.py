from app import db
import time
from math import floor


class Building(db.Model):
    __tablename__ = "building"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    full_name = db.Column(db.String(256), unique=True, nullable=False)

    rooms = db.relationship('Room', backref='owning_building', lazy=True)

    def __repr__(self):
        return "<Building: {}>".format(self.name)

    def __init__(self, name, full_name=""):
        self.name = name
        self.full_name=full_name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'full_name': self.full_name
            }


class Room(db.Model):
    """"""
    __tablename__ = "room"

    id = db.Column(db.Integer, primary_key=True)
    roomnumber = db.Column(db.String, nullable=False)

    days = db.relationship('Day', backref='owning_room')

    building_id = db.Column(db.Integer, db.ForeignKey("building.id"), nullable=False)

    # Note, 1440 is the maximum number of minutes any room can be free, because it's 24*60.
    minutes_free = 1440
    
    time_room_free = "Free Rest of Day"
    time_list = []

    def __lt__(self, other):
        return other.minutes_free < self.minutes_free

    def time_in_minutes(self, input):
        string = input.split(":")[0] + input.split(":")[1][0:2]
        number = int(string)
        if "PM" in input and number < 1200:
            number = number + 1200
        elif "AM" in input and number >= 1200 and number <= 1259:
            number = number - 1200
#         print("Number is:", number)
        number = (number // 100) * 60 + int(string[len(string)-2:])
        return number

    def free_time(self, day, time):
        """ 
        This function generates the amount of time the room is free. 
        It stores the free time locally in time_room_free
        It stores the minutes free in minutes_free
        It stores the list of all class times as tuples in time_list.
        These values are later used to generate info about the rooms in the templates. The use case is to run this before doing any analysis on the rooms.
        """
        # Start out with a fresh list of times to generate. This prevents the list from getting full if this function is called more than once.
        self.time_list.clear()
        time = self.time_in_minutes(time)
        today = 0

        for d in self.days:
            if d.name == day:
                today = d 

        if today == 0:
            return "Free Rest of Day"
        else:

            # Parse out all the times ranges, so that we can use them to build the calendar later. 
            times = today.ranges.split("##")
            for i in range(len(times)):
                times[i] = times[i].replace("#", "")
                t = times[i].split('-')
                start = self.time_in_minutes(t[0])
                end = self.time_in_minutes(t[1])
                self.time_list.append((start,end))
            
            for class_time in self.time_list:
                start = class_time[0]
                end = class_time[1]

                if time < start:

                    minutes_free = (start - time) % 60
                    hours_free = (start - time) // 60

                    self.minutes_free = start - time
                    self.time_room_free = "Free for: " + str(hours_free) + " hrs " + str(minutes_free) + " mins"
                    return self.time_room_free
                elif time < end:
                    minutes_free = (end - time) % 60
                    hours_free = (end - time) // 60
                    self.minutes_free = -(end - time)
                    self.time_room_free = "Not free for: " + str(hours_free) + " hrs " + str(minutes_free) + " mins"
                    return self.time_room_free
        return "Free Rest of Day"

    def __repr__(self):
        return "Room is: {}, Building is: {}".format(self.roomnumber, self.owning_building.name)

    def __init__(self, roomnumber, building_id):
        self.roomnumber = roomnumber
        self.building_id = building_id

    def serialize(self):
        return {
            'id': self.id,
            'roomnumber': self.roomnumber,
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
        return "On: {} Time ranges are: {}".format(self.name, self.ranges)

    def __init__(self, name, ranges, room_id):
        self.name = name
        self.ranges = ranges
        self.room_id = room_id
