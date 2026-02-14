import os

hostname = os.uname().nodename

cpu_usage = "N/A"
memory_usage = "N/A"

print("System INfo")
print("-----------------")
print("Hostname", hostname)
print("CPU Usage:", cpu_usage)
print("Memory Usage:", memory_usage)
