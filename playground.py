#!/usr/bin/env python3

import datetime
import arrow
import ics

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

calendarData = calendarData.split("//")

# remove empty items
for item in calendarData:
    if not item.rstrip():
        calendarData.remove(item)

for i in range(len(calendarData)):
    # print(calendarData[i])
    entryList = calendarData[i].split("/")
    entry = dict()
    entry["name"] = entryList[0].strip()
    entry["location"] = entryList[1].strip()
    entry["description"] = entryList[2].strip()
    entry["begin"] = arrow.now()
    entry["end"] = arrow.now()
    calendarData[i] = entry
    

    
# Generate ics file    
# -----------------
    
calendarAsICS = ics.Calendar()
    
    
# write output to file
# --------------------

outfile = open("./privateData/outfile.ics", "w", encoding="utf-8")
# outfile.write(format(calendarData))
outfile.writelines(calendarAsICS)
outfile.close()
