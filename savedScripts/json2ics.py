#!/usr/bin/env python3

import datetime
import arrow
import ics

testOutput = list()

# set up test data for calendar generation
# ----------------------------------------

calendarData = """
//
first meeting/
your office/
we will discuss stuff.
//
second meeting/
my office/
we will talk some more.
//
"""

# import into json object

# split into events
calendarData = calendarData.split("//")

# remove empty items
for item in calendarData:
    if not item.rstrip():
        calendarData.remove(item)

# loop through events
for i in range(len(calendarData)):
    # split event into fields
    entryList = calendarData[i].split("/")
    # write fields to dict
    entry = dict()
    entry["name"] = entryList[0].strip()
    entry["location"] = entryList[1].strip()
    entry["description"] = entryList[2].strip()
    entry["begin"] = arrow.now()
    entry["end"] = arrow.now()
    # replace string with dict in original data
    calendarData[i] = entry
  
# test output from json
# ---------------------

# from pprint import pprint
# pprint(calendarData)  

# [{'begin': <Arrow [2018-10-17T10:11:45.763299+02:00]>,
  # 'description': 'we will discuss stuff.',
  # 'end': <Arrow [2018-10-17T10:11:45.763299+02:00]>,
  # 'location': 'your office',
  # 'name': 'first meeting'},
 # {'begin': <Arrow [2018-10-17T10:11:45.763299+02:00]>,
  # 'description': 'we will talk some more.',
  # 'end': <Arrow [2018-10-17T10:11:45.763299+02:00]>,
  # 'location': 'my office',
  # 'name': 'second meeting'}]
    
# Generate ics file    
# -----------------
    
# generate ics object
calendarAsICS = ics.Calendar()

# loop through calendar json and write events to ics object
for entry in calendarData:
        newEntry = ics.Event()
        for field in entry:
                # create a string for exec() that takes field name from key and field value from value
                execStr = "newEntry.{} = \"{}\"".format(field,entry[field])
                exec(execStr)
        calendarAsICS.events.add(newEntry)
    

    
# write output to file
# --------------------

outfile = open("./privateData/outfile.ics", "w", encoding="utf-8")

outfile.writelines(calendarAsICS)

for item in testOutput:
    outfile.write("{}\n".format(item))

    outfile.close()
