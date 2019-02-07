from flask import render_template, request

from app import app

from app.forms import LoginForm


@app.route("/")
def home():
    form = LoginForm()
    return render_template('home.html', form=form)


@app.route('/result', methods=['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html", result=result)
   elif request.method == 'GET':
       result = request.args
       return render_template("result.html", result=result)

@app.route("/add")
def add_building():
    name=request.args.get('name')
    try:
        building=Building(
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
        building=Building.query.all()
        return  jsonify([e.serialize() for e in building])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        building=Building.query.filter_by(id=id_).first()
        return jsonify(building.serialize())
    except Exception as e:
	    return(str(e))


@app.route("/add/form",methods=['GET', 'POST'])
def add_building_form():
    if request.method == 'POST':
        name=request.form.get('name')
        try:
            building=Building(
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
