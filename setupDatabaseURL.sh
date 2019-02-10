#!/bin/bash
# Run this script as ./setupDatabaseURL 'herokuURLOfPostgresDatabase'. Then this will set the system variable linking the database, without compromising the password to the database on github.
export DATABASE_URL=$1
