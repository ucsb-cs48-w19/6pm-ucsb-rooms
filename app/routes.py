from flask import render_template, request, jsonify
from app import app
from app import db
from models import Building, Room

from app.forms import LoginForm
from app.time_formatter import get_day_pst
from app.time_formatter import get_time_pst

# from datetime import date
# import calendar


@app.route("/")
def home():
    #form = LoginForm()
    #return render_template('home.html', form=form)
    buildings = Building.query.all()

    return render_template('home.html', placeholder="Building", room_placeholder="", buildings=buildings)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        return render_template("result.html", result=result)
    elif request.method == 'GET':
        result = request.args.to_dict()
        result['Building'] = request.args.get('Building').upper();
        result['Room'] = request.args.get('Room');
        #print("THIS IS THE DIR========",dir(result))
        if (result.get("Day") == "TODAY"):
            result["Day"] = get_day_pst()
        #print("RESULTS ARE A: ", help(result))
        name = result.get("Building")
        rn = request.args.get('Room')
        allBuildings = ""
        try:
            # print(Room.query.first())
            # print(Building.query.first().rooms)

             building = Building.query.filter_by(name=name).first()
#              print("We got the building:",name,". It look like:",building)
             rooms = []
             if (building != None):
                rooms = building.rooms
                for r in rooms:
                    r.free_time(result.get("Day"), get_time_pst())

                rooms.sort()
#                 print("YOUR ROOMS SORTED LOOK LIKE",rooms)
             else:
                 buildings = Building.query.all()
                 return render_template("home.html", placeholder='Invalid Building', buildings=buildings)

             if(rn != ""):
                 id=building.id
                 room = Room.query.filter(Room.building_id==id, Room.roomnumber==rn).first()
                 if(room!=None):
                     time = get_time_pst()
                     if (result.get("Day") == "TODAY"):
                         result["Day"] = get_day_pst()
                     room.free_time(result.get("Day"),get_time_pst())
                     return render_template("room.html", result=result, room=room, time=time)
                 else:
                    buildings = Building.query.all()
                    return render_template("home.html", room_placeholder='Invalid Room number', buildings=buildings)

             return render_template("result.html", result=result, building=building, rooms=rooms, time=get_time_pst())#get_time_pst())
        except Exception as e:
            return(str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')


@app.route('/room', methods=['GET'])
def room():
    """Display a specific room. Sytntax is as follows: /room?Building=HSSB&Room=2001A"""
    result = request.args.to_dict()
    time = get_time_pst()
    if (result.get("Day") == "TODAY"):
        result["Day"] = get_day_pst()
    id = int(request.args.get('BuildingID'))
    #building = Building.query.filter_by(name=name).first()

    rn = request.args.get('Room')

    room = Room.query.filter(Room.building_id==id, Room.roomnumber==rn).first()
    room.free_time(result.get("Day"),get_time_pst())
#    print(room.time_list)
#     print(room.free_time(result.get("Day"),get_time_pst()))
    return render_template("room.html", result=result, room=room, time=time)


if __name__ == '__main__':
    app.run(debug=True)
