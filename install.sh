#!/bin/sh
autokeyDir="$HOME/.config/autokey/"
echo "Creating "$autokeyDir"data/Quickey/ directory..."
mkdir -p $autokeyDir"data/Quickey"
echo "done"
echo "Copying "$autokeyDir"data/Quickey/ directory..."
cp -r Quickey $autokeyDir"data/"
echo "done"
echo "Creating "$autokeyDir"quickey.py/ directory..."
mkdir -p $autokeyDir"quickey.py" 2> /dev/null
echo "done"
echo "Copying "$autokeyDir"quickey.py/quickey.py file..."
cp quickey.py $autokeyDir"quickey.py"
echo "done"
