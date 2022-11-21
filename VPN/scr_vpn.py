import subprocess

# This is our shell command, executed in subprocess.

p = subprocess.run("cp", "dirA/file", "dirB")



import subprocess

# This is our shell command, executed by Popen.

p = subprocess.Popen("ls -lh", stdout=subprocess.PIPE, shell=True)

print(p.communicate())






with subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE) as proc:
   print(proc.stdout.read())








# pip install Command


import command 

res = command.run(['ls']) 

print(res.output) 
print(res.exit)




import command

def debugger(text):     
    print(text)
  
res = command.run(['ls'], debug=debugger) 

print(res.output) 
print(res.exit)



import subprocess

subprocess.run(["myscript.sh", "--input_file=input.txt"])