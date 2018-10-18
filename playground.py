#!/usr/bin/env python3

import ics
import re

from pprint import pprint

output = []



icsData = ics.Calendar()
newEntry = None
newEntryRegex = r"""Do\. (\d{2})\.\s?(\d{2})\.\s?(\d{4})\s?:\s*[„“]?([^„“]*)[„“]?\s*"""


infile = open("privateData/infile.txt", "r", encoding="utf-8")
for line in infile:
    line = line.rstrip()
    # output.append(line)
    newEntryEval = re.match(newEntryRegex,line)
    if newEntryEval:
        output.append(line)
        output.append(newEntryEval.groups())
    
    
infile.close()



icsData.events.add(newEntry)

# for line in output:
    # icsData.events.add(newEntry)
    # newEntry = ics.Event()

# write output
# ------------

outfile = open("privateData/outfile.ics", "w", encoding="utf-8")

outfile.writelines(icsData)

for line in output:
    outfile.write(format(line))
    outfile.write("\n")
    
outfile.close()