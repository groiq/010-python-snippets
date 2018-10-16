#!/usr/bin/env python3



# set up test data for calendar generation

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
    calendarData[i] = entry
    

        
# cd2 = calendarData.split("---")
# cd3 = list()
# for item in cd2:
    # cd3.append(item.split("\n"))

# calendarData = cd3

# infile = open("./privateData/infile.txt", "r", encoding="utf-8")
# print(infile)
# for line in infile:
    # print(line.rstrip())
# infile.close()

outfile = open("./privateData/outfile.ics", "w", encoding="utf-8")
outfile.write(format(calendarData))
outfile.close()