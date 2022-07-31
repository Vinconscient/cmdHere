import subprocess,os
path = 'cd ' + str(os.getcwd())
process = subprocess.run(["start", "cmd", "/K",path], shell=True)
