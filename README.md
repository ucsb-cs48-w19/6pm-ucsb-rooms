# **Where is Every1?**

## Summary

Find a nice place to study, meet, utilize space within the school all in one app.


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
six(1.12.0)
SQLAlchemy(1.2.17)
Werkzeug(0.14.1)

## **Installation Steps**
**On Linux:**

`sudo apt install python3`

`sudo apt install pip3`

`pip3 install flask`

`pip3 install selenium`

Continue to pip3 install each dependancy listed above in the previous row until they are all satisfied. You can check pip3 list to see what is already installed. Install flask first, which will include many of the other items automatically. 

## **Functionality**

To deploy to heroku, you will need to set up a heroku remote. 
First, make sure you have the heroku CLI installed, then run the command:
heroku git:remote -a ucsb-rooms

For users use the link above to see the app running. 

## **Running Locally**

For developers, after cloning the repo and installing dependancies, run python3 ./app.py to start the project locally.
