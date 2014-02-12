# Regexp of window title or WM_CLASS.
regexp = " - Google Chrome$"
# Start up command.
command = "google-chrome"
# Options
options = "-a"

# Call the main routine(Don't change me!!).
system.exec_command('python ~/.config/autokey/quickey.py/quickey.py %s "%s" "%s"' % (options, regexp, command), getOutput=True)
