#!/usr/bin/env python3

import ics

from pprint import pprint

output = []

infile = open("privateData/infile.txt", "r", encoding="utf-8")
for line in infile:
    line = line.rstrip()
    output.append(line)
infile.close()


icsData = ics.Calendar()



# write output
# ------------

outfile = open("privateData/outfile.ics", "w", encoding="utf-8")

outfile.writelines(icsData)

for line in output:
    outfile.write(format(line))
    outfile.write("\n")
    
outfile.close()