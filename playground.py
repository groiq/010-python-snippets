#!/usr/bin/env python3

from pprint import pprint

# CSV to table

# read a table from a csv file and render it as an html table with empty fields

# read data



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

output.write("Content goes here\n")



output.write(footer)


output.close()
