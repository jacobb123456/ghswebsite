#!ghswebsite/bin/python3
import sys
import datetime
from app import db
from models import Hour


def add(user, hours, desc, item):
    isItem = True
    if item == "False":
        isItem = False
    newHour = Hour(datetime.datetime.now(), user, float(hours), desc, isItem)
    db.session.add(newHour)
    db.session.commit()
    print("New hour entry for " + user + " created: " + desc)


def delete(desc):
    Hour.query.filter_by(desc=desc).delete(synchronize_session=False)
    db.session.commit()

if len(sys.argv) >= 3:
    if sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == "del":
        delete(sys.argv[2])
    else:
        print(
            "usage: add or delete hour database entries <20xxusername> <number of hours> <description> <is item>")
        exit(1)
else:
    print("usage: add or delete hour database entries <20xxusername> <number of hours> <description> <is item>")
    exit(1)
