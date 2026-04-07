import re

log_file="sample.log"

pattern_error=r"ERROR"
pattern_warning=r"WARNING"

error_count=0
warning_count=0

with open(log_file, "r") as file:
  for line in file:
    if re.search(pattern_error, line):
       error_count+=1
    elif re.search(pattern_warning, line):
       warning_count+=1

errors=[]

with open(log_file, "r") as file:
  for line in file:
    if re.search(pattern_error, line): 
       errors.append(line.strip())

print("\nERROR Details:")
for e in errors:
  print(e)


with open("report.txt", "w") as report:
   report.write("LOG SUMMARY\n")
   report.write("-----------------\n")
   report.write(f"ERRORS:{error_count}\n")
   report.write(f"WARNING:{warning_count}\n")
   
   report.write("ERROR Details:\n")
   for e in errors:
     report.write(e+"\n")
