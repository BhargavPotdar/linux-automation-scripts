import re

pattern=r"ERROR|WARNING"

with open("sample.log", "r") as file:
  for line in file:
    if re.search(pattern,line):
       print(line.strip())
