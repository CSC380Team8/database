#!/usr/bin/python
import MySQLdb

database = raw_input("Database:")
user = raw_input("Username:")
password = raw_input("Password:")

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        user=user,         # your username
        passwd=password,  # your password
        db=database)        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM Observation")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]

db.close()
