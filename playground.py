#!/usr/bin/env python3

from pprint import pprint

# CSV to table

# read a table from a csv file and render it as an html table with empty fields

# read data

import csv

with open("./publicTestData/csv2table.csv","r",encoding="utf-8") as dataFile:
    data = csv.DictReader(dataFile, delimiter=";")

    for row in data:
        #print(row)
        print(row["Name"])
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



tableFooter="""
</table>
"""

output.write(tableHeader)

tablePlaceholder = """
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
<tr><td>&nbsp;</td><td>&nbsp;</td><td>&nbsp;</td></tr>
"""

output.write(tablePlaceholder)

output.write(tableFooter)


output.write(footer)


output.close()
