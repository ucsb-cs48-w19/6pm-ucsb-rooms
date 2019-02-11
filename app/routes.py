from flask import render_template, request, jsonify

from app import app

from app import db

from models import Building, Room

from app.forms import LoginForm


@app.route("/")
def home():
    #form = LoginForm()
    #return render_template('home.html', form=form)
    return render_template('home.html', placeholder="Building")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
    elif request.method == 'GET':
        result = request.args
        name = request.args.get('Building')
        allBuildings = ""
        try:
            # print(Room.query.first())
            # print(Building.query.first().rooms)
           
             building = Building.query.filter_by(name=name).first()
             rooms = []
             if (building != None):
                rooms = Room.query.all()
             else:
                 return render_template("home.html", placeholder='Invalid Building')
                 
            # building=Building(name=name)
            # db.session.add(building)
            # db.session.commit()
#            buildingList= []
#            try:
#                 buildingList=Building.query.all()
#               # allBuildings = jsonify([e.serialize() for e in buildingList])
#                 for e in buildingList:
#                   allBuildings+= e.name + " "
#            except Exception as e:
#       	     return( "getall failed" , str(e))
            # return "hi"
#            print (allBuildings)
             return render_template("result.html", result=result, table="Building added. building id={}".format(building.id), rooms=rooms)
        except Exception as e:
            return(str(e))


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
