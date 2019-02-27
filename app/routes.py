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

    return render_template('home.html', placeholder="Building", buildings=buildings)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
        return render_template("result.html", result=result)
    elif request.method == 'GET':
        result = request.args.to_dict()
        result['Building'] = request.args.get('Building').upper();
        #print("THIS IS THE DIR========",dir(result))
        if (result.get("Day") == "TODAY"):
            result["Day"] = get_day_pst()
        #print("RESULTS ARE A: ", help(result))
        name = result.get("Building")
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

             return render_template("result.html", result=result, building=building, rooms=rooms)#get_time_pst())
        except Exception as e:
            return(str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')


@app.route('/room', methods=['GET'])
def room():
    """Display a specific room. Sytntax is as follows: /room?Building=HSSB&Room=2001A"""
    result = request.args
    id = int(request.args.get('BuildingID'))
    #building = Building.query.filter_by(name=name).first()

    rn = request.args.get('Room')
    
    room = Room.query.filter(Room.building_id==id, Room.roomnumber==rn).first()
    room.free_time(result.get("Day"),get_time_pst())
    print(room.time_list)
#     print(room.free_time(result.get("Day"),get_time_pst()))

    return render_template("room.html", result=result, room=room)
    

@app.route("/add")
def add_building():
    name = request.args.get('name')
    try:
        building = Building(
            name=name
        )
        db.session.add(building)
        db.session.commit()
        return "Building added. building id={}".format(building.id)
    except Exception as e:
	    return(str(e))


@app.route("/getall")
def get_all():
    try:
        building = Building.query.all()
        allBuildings = jsonify([e.serialize() for e in building])
        print (allBuildings)
        return  jsonify([e.serialize() for e in building])
    except Exception as e:
	    return(str(e))


@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        building = Building.query.filter_by(id=id_).first()
        return jsonify(building.serialize())
    except Exception as e:
	    return(str(e))


@app.route("/add/form", methods=['GET', 'POST'])
def add_building_form():
    if request.method == 'POST':
        name = request.form.get('name')
        try:
            building = Building(
                name=name
            )
            db.session.add(building)
            db.session.commit()
            return "Building added. building id={}".format(building.id)
        except Exception as e:
            return(str(e))
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
