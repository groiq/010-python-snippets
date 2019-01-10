#!/usr/bin/env python3

from pprint import pprint

# CSV to table

# read a table from a csv file and render it as an html table with empty fields

# read data

import csv

data = []

with open("./publicTestData/csv2table.csv","r",encoding="utf-8") as dataFile:
    dataSource = csv.DictReader(dataFile, delimiter=";")

    for row in dataSource:
        #print(row)
        tempDict = {}
        tempDict["Name"] = row["\ufeffName"]
        tempDict["Menge"] = row["Menge"]
        tempDict["Stückzahl"] = row["Stückzahl"]
        #for field in row:
         #   tempDict[field] = row[field]
        #tempDict["Name"] = row["Name"]
        data.append(tempDict)
        

    #for row in data:
        #print(row)
       # print(row["Name"])
        #print(row["Menge"])
        #for field in row:
         #   print(field)

    
# write html output

header = """<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>csv2table</title>
  </head>
  <body>

"""

footer = """

  </body>
</html>"""

output = open("./publicTestData/csv2table.html","w",encoding="utf-8")

output.write(header)

output.write("<h2 align='center'>This is a csv file rendered as a table</h2>\n\n")

tableHeader="""
<table border='1' width='100%'>
"""

tablePlaceholder = """
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
"""



tableFooter="""
</table>
"""

output.write(tableHeader)

#output.write(tablePlaceholder)

print(data)
for row in data:
    output.write("<tr>\n")
    output.write("<td colspan='8'>{}</td>".format(row["Name"]))
    output.write("<td>{}</td>".format(row["Menge"]))
    output.write("<td>{}</td>".format(row["Stückzahl"]))
    output.write("</tr>\n<tr>")
    for i in range(10):
        output.write("<td>&nbsp;</td>")
    output.write("\n")
    #output.write(

    output.write("</tr>\n")


output.write(tableFooter)


output.write(footer)


output.close()
