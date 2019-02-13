# **Where is Every1?**

## Summary

Find a nice place to study, meet, and utilize space at UCSB all in one app.


This web app scrapes the course schedules at UCSB and then allows a user to search for an available room. This means that people can easily find space to meet up or study, and know how long a classroom is empty.

**For Users:**
Use link - [https://ucsb-rooms.herokuapp.com/](https://ucsb-rooms.herokuapp.com/)

Old Project link using Java - [https://ucsb-cs56-where-is-every1.herokuapp.com](https://ucsb-cs56-where-is-every1.herokuapp.com)

**For Developers:**

This project uses the Flask framework.

Use the following steps:

## Installation

**Prerequisites:**

python3, pip3, selenium, flask

Deploying requiremements and versions listed below. The version doesn't matter that much, as long as some version is installed. These requirements can be found in requirements.txt.

astropy(3.1.1)
alembic(1.0.7)
Click(7.0)
Flask(1.0.2)
Flask-Migrate(2.3.1)
Flask-Script(2.0.6)
Flask-WTF(0.14.2)
Flask-SQLAlchemy(2.3.2)
gunicorn(19.9.0)
itsdangerous(1.1.0)
Jinja2(2.10)
Mako(1.0.7)
MarkupSafe(1.1.0)
psycopg2-binary(2.7.7)
python-dateutil(2.7.5)
python-editor(1.0.3)
selenium(3.141.0)
six(1.12.0)
SQLAlchemy(1.2.17)
Werkzeug(0.14.1)
urllib3(1.24.1)
WTForms(2.2.1)

## **Installation Steps**
**On Linux:**

`sudo apt install python3`

`sudo apt install pip3`

`pip3 install flask`

`pip3 install selenium`

Continue to pip3 install each dependancy listed above in the previous row until they are all satisfied. You can check pip3 list to see what is already installed. Install flask first, which will include many of the other items automatically. 

## **Functionality**
**Note you cannot deploy to the below herokuAPP unless you have logged in at heroku, and are a collborator on the HerokuAPP**

To deploy to heroku, you will need to set up a heroku remote. 
First, make sure you have the heroku CLI installed, then run the command:
heroku git:remote -a ucsb-rooms

For users use the link above to see the app running. 

## **Running Locally**

For developers, after cloning the repo and installing dependancies, run command "**python3 ./app.py**" to start the project locally.

## **Building the Database locally**
We cannot give everyone the database credentials. To build the database locally and run the app follow these steps:
1. In config.py, comment this line: SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 
  and uncomment this line: SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
2. If you want to build the entire database it will take 20-40 minutes. 
If you would like to build a smaller version of the database that will take 2-3 and still give you a lot of function. 
To build the large database skip this step. To build the smaller one, in file buildDatabase.py, change line 10 from:scrape.iterateSubjects() to scrape.iterateAnthropology()
3. build the database locally by typing on terminal: python3 buildDatabase.py. 
  This database will be built using SQLite to site.db
4. Run the app locally using app.py
