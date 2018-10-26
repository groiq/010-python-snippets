#!/usr/bin/env python3

from pprint import pprint
import csv

csvData = csv.DictReader(open("./privateData/uniteCSV.csv", "r", encoding="utf-8-sig"), delimiter=";")
urlList = open("./privateData/uniteCSV.txt", "r", encoding="utf-8").readlines()
# print(type(urlList))
# pprint(urlList)


data = list()
urlNumber = 0

for row in csvData:
    # print(row)
    # print("------------------------------------------------------")
    # for item in row:
        # print(item)
        # print(row[item])
    # print(row["Name"])
    # print(row["Berufe"])
    row["url"] = urlList[urlNumber]
    urlNumber += 1
    data.append(row)
    
# write json to file
jsonFile = open("./privateData/uniteCSVJson.json", "w", encoding="utf-8")
jsonFile.write(format(data))
jsonFile.close()

# generate HTML

header = """
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>unite csv</title>
  </head>
  <body>
  
"""

footer = """
  </body>
</html>
"""

bod = list()
bod.append("<table>")
for dataset in data:
    bod.append("<tr>")
    # bod.append("<td>{}</td>".format(dataset["Name"]))
    bod.append("</tr>")
bod.append("</table>")

htmlOutput = open("./privateData/uniteCSVOut.html", "w", encoding="utf-8")
htmlOutput.write(header)
# htmlOutput.write("<pre>")
# htmlOutput.write(format(data))
# htmlOutput.write("</pre>")
for line in bod:
    htmlOutput.write(line)
    htmlOutput.write("\n")
htmlOutput.write(footer)
htmlOutput.close()
    
# pprint(data)
