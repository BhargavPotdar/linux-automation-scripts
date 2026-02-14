import os

def print_header():
 print("System Info")
 print("-----------------")

def check_services(service_list):
 for s in services:
    print("Checking service:", s)

hostname = os.uname().nodename
services = ["ssh", "cron", "nginx"]

print_header()

print("Hostname", hostname)

check_services(services)
