# Regexp of window title.
regexp = "- GVIM$"
# start up command.
command = "gvim"

# main routine(Don't change me!!).
system.exec_command('python ~/.config/autokey/quickey.py/quickey.py "%s" "%s"' % (regexp, command), getOutput=True)
