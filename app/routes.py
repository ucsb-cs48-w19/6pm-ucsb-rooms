from flask import render_template, request, jsonify

from app import app

from app import db

from models import Building, Room

from app.forms import LoginForm

from datetime import date
import calendar

@app.route("/")
def home():
    #form = LoginForm()
    #return render_template('home.html', form=form)
    buildings = Building.query.all()

    return render_template('home.html', placeholder="Building", buildings=buildings)


@app.route('/result', methods=['POST', 'GET'])
def result():
<<<<<<< HEAD
   if request.method == 'POST':
      result = request.form
      return render_template("result.html", result=result)
   elif request.method == 'GET':
       result = request.args
       name=request.args.get('Building')
       allBuildings= ""
       try:
           building=Building(
               name=name
           )
           db.session.add(building)
           db.session.commit()
           buildingList= []
           try:
               #
                buildingList=Building.query.all()
              # allBuildings = jsonify([e.serialize() for e in buildingList])
                for e in buildingList:
                  allBuildings+= e.name + " "
           except Exception as e:
       	    return( "getall failed" , str(e))
           #return "hi"
           print (allBuildings)
           return render_template("result.html", result=result, table="Building added. building id={}".format(building.id), buildingList=buildingList)
       except Exception as e:
           return(str(e))
=======
    if request.method == 'POST':
        result = request.form.to_dict()
        return render_template("result.html", result=result)
    elif request.method == 'GET':
        result = request.args.to_dict()
        #print("THIS IS THE DIR========",dir(result))
        if (result.get("Day") == "TODAY"):
            my_date = date.today()
            result["Day"] = calendar.day_name[my_date.weekday()][0]
        #print("RESULTS ARE A: ", help(result))
        name = request.args.get('Building')
        allBuildings = ""
        try:
            # print(Room.query.first())
            # print(Building.query.first().rooms)
           
             building = Building.query.filter_by(name=name).first()
             print("We got the building:",name,". It look like:",building)
             rooms = []
             if (building != None):
                rooms = building.rooms
             else:
                 buildings = Building.query.all()
                 return render_template("home.html", placeholder='Invalid Building', buildings=buildings)

             return render_template("result.html", result=result, table="Building added. building id={}".format(building.id), rooms=rooms)
        except Exception as e:
            return(str(e))
>>>>>>> ade8e0326c6e2d948c3a454030396e72f52fe83b

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

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
