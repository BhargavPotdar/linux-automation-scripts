O
Ximport subprocess

commands=[["df", "-h"], ["free", "-m"], ["uptime"]]

for cmd in commands:
    result=subprocess.run(cmd, capture_output=True, text=True)
    print(f"\nCommand: {' '.join(cmd)}")
    print(result.stdout)


