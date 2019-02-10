#!/bin/bash
heroku run python3 manage.py db upgrade
#add '--app appNameHere' to specify a particular app
