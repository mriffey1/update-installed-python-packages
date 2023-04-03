# Updating installed Python packages

### This script was created on Windows (modification may be required to run on other systems)

This little project came about when realizing there was no easy way to mass update installed Python packages.

The script will obtain a list of outdated packages using `pip list` and formatting the list as JSON.

From there - the script will get the name of each package, format it with the command needed to upgrade it and add it to a list. Afterwards, using a for loop, each command in the list will be ran and each package updated.
