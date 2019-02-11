from app import db

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
    ranges = db.Column(db.String)
    room_type = db.Column(db.String)

    building_id = db.Column(db.Integer, db.ForeignKey("building.id"), nullable=False)
    
#    building = db.relationship("Building", backref=db.backref(
#        "room", order_by=id), lazy=True)

    def __repr__(self):
        return "Room is: {}, Building is: {}, Time Ranges are: {}".format(self.roomnumber, self.owning_building.name, self.ranges)

    def __init__(self, roomnumber, ranges, room_type, building_id):
        self.roomnumber = roomnumber
        self.ranges = ranges
        self.room_type = room_type
        self.building_id = building_id

    def serialize(self):
        return {
            'id': self.id,
            'roomnumber': self.roomnumber,
            'ranges': self.ranges,
            'room_type': self.room_type
            }
    def add_timerange(self, range):
        ranges += range