import subprocess
import threading

commands=[["df","-h"], ["free", "-m"], ["uptime"]]

def run_command(cmd):
    result=subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)

threads=[]

for cmd in commands:
    t=threading.Thread(target=run_command, args=(cmd,))
    t.start()


