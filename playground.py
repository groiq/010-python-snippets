#!/usr/bin/env python3

from pprint import pprint
import csv

csvData = csv.DictReader(open("./privateData/uniteCSV.csv", "r", encoding="utf-8"))

pprint(csvData)
