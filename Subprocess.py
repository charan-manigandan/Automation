import subprocess

cmd = ["ls", "-l"]
# remember if shell is false the shell command is returns output normally and shell is true then it returns the path od the process
sp = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rt = sp.wait()
out, err = sp.communicate()
print(out)
print(err)
