import subprocess
import os


fd = open('stdout.txt', 'w')
with subprocess.Popen(["ls", "-l"], shell=False, stdout=fd, close_fds=True) as proc:
    # print(proc.stdout.read())
    pass
out = subprocess.check_output('ls -l', shell=True)
print(out)

command = "python3 " + os.path.dirname(os.path.realpath(__file__)) + "/ss.py"
print(command)
sub = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
sub.wait()
print(sub.poll())
