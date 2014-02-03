import subprocess
import re
import sys

# Main routine.
def go(target_string, path):
    wmctrl_list = exec_command("wmctrl -l").split("\n")

    pattern = re.compile(target_string)
    if any(pattern.search(line) for line in wmctrl_list):
        title = exec_command("wmctrl -l | awk '/%s/ {for(i=4;i<NF;++i){printf(\"%%s \",$i)}print $NF}'" % target_string)
        exec_command("wmctrl -a \"%s\"" % title)
    else:
        exec_command(path)

# Execute system command by argument.
def exec_command(command):
    return subprocess.Popen(
            command,
            shell=True,
            bufsize=-1,
            stdout=subprocess.PIPE
            ).stdout.read()[:-1]

# Call the main routine.
go(sys.argv[1], sys.argv[2])
