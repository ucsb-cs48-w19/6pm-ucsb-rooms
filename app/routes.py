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


if __name__ == '__main__':
    app.run(debug=True)
