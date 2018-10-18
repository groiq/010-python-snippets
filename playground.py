#!/usr/bin/env python3

output = []

infile = open("privateData/infile.txt", "r", encoding="utf-8")
for line in infile:
    line = line.rstrip()
    output.append(line)
infile.close()





outfile = open("privateData/outfile.ics", "w", encoding="utf-8")
for line in output:
    outfile.write(format(line))
    outfile.write("\n")
outfile.close()