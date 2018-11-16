#!/usr/bin/env python3

infile = open("outfile.txt", "r", encoding="utf-8").read()
magicNum = int(infile) + 1

outfile = open("outfile.txt", "w", encoding="utf-8")

outfile.write(format(magicNum))