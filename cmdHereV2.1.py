import subprocess,os
path = 'cd ' + str(os.getcwd())
process = subprocess.run(["start", "cmd", "/K",path,"&& type C:\\Users\\Sylvain\\style.txt"], shell=True)