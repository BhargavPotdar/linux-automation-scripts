import re

with open("sample.log", "r") as file:
 for line in file:
   if re.search("ERROR", line):
      print(line.strip())



