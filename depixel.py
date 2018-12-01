import subprocess
import sys
InputFiles=[] 
for i in range(len(sys.argv)):
    if i == 0:
        continue
    InputFiles.append(sys.argv[i])
    command="potrace "+InputFiles[i-1]+" -b pdf"
    a=subprocess.Popen(command,shell=True)
    