#!/bin/bash

LOGFILE="/tmp/system_health.log"

check_disk() {
      echo "Disk Usage: "
      df -h /
}

check_memory() {
      echo "Memory Usage: "
      free -m
}

echo "System Health Check" >>  "$LOGFILE"
check_disk >> "$LOGFILE"
check_memory >> "$LOGFILE"
