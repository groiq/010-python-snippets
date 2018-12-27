#!/usr/bin/env python3

from pprint import pprint
import os

#print("hello")
#print(os.listdir("./privateData/renameFile"))

# parse categories

categories = []

catsRaw = open("./privateData/renameFileCategories.txt","r",encoding="utf-8")

for line in catsRaw:
    line = line.strip()
    #print(line)
    vals = line.split(",")
    #print(data)
    categories.append(vals)

# pprint(categories)

# Cycle through all possible combinations of categories

# for i in range(len(categories)):
#     print(i)
#     print(categories[i])

def cycleThroughCategory(catIndex):
    category = categories[catIndex]
    print(category)
    nextIndex = catIndex + 1
    if nextIndex < len(categories):
        nextCat = cycleThroughCategory(nextIndex)
    return category


 

cycleThroughCategory(0)

# rename each file from os.listdir with the values from that cycle

