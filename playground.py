#!/usr/bin/env python3



# set up test data for calendar generation

calendarData = """
---
first meeting
your office
we will discuss stuff.
---
second meeting
my office
we will talk some more.
---
"""

# calendarData = calendarData.split("---")



# infile = open("./privateData/infile.txt", "r", encoding="utf-8")
# print(infile)
# for line in infile:
    # print(line.rstrip())
# infile.close()

outfile = open("./privateData/outfile.ics", "w", encoding="utf-8")
outfile.write(calendarData)
outfile.close()