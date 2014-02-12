# Regexp of window title or WM_CLASS.
regexp = "^gvim.Gvim$"
# Start up command.
command = "gvim"
# Options
options = "-c -r"

# main routine(Don't change me!!).
system.exec_command('python ~/.config/autokey/quickey.py/quickey.py %s "%s" "%s"' % (options, regexp, command), getOutput=True)
