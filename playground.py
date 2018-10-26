#!/usr/bin/env python3

from pprint import pprint
import csv

csvData = csv.DictReader(open("./privateData/uniteCSV.csv", "r", encoding="utf-8-sig"), delimiter=";")
urlList = open("./privateData/uniteCSV.txt", "r", encoding="utf-8").readlines()
# print(type(urlList))
pprint(urlList)


data = list()

for row in csvData:
    # print(row)
    # print("------------------------------------------------------")
    # for item in row:
        # print(item)
        # print(row[item])
    # print(row["Name"])
    # print(row["Berufe"])
    data.append(row)
    
pprint(data)
