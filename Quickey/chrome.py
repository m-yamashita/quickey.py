# Regexp of window title.
regexp = " - Google Chrome$"
# Start up command.
command = "google-chrome"

# Call the main routine(Don't change me!!).
system.exec_command('python ~/.config/autokey/quickey.py/quickey.py "%s" "%s"' % (regexp, command), getOutput=True)
