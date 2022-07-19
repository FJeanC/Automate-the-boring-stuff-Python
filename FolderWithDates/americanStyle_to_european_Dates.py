#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.


from calendar import day_abbr
import shutil, os, re

# Create a regex that matches files  with the American date format. 
# MM-DD-YYYY
datePattern = re.compile(r''' 
    ^(.*?)                    # All text before the date
    ((0|1)?\d)-               # one or two digits for the month
    ((0|1|2|3)?\d)-           # one or two digits for the day
    ((19|20)\d\d)             # four digits for the year
    (.*?)$                   #all text after the date
''', re.VERBOSE)

# Loop over the files in the working directory
for amerFile in os.listdir('.'):
    mo = datePattern.search(amerFile)
    if mo == None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    euroFileName = beforePart + dayPart + '-' + monthPart+'-'+yearPart+ afterPart
    # Get the full absolute paths.
    absWorkingDirectory = os.path.abspath('.')
    amerFile = os.path.join(absWorkingDirectory, amerFile)
    euroFileName = os.path.join(absWorkingDirectory, euroFileName)

    # Rename the files.
    print(f'Renaming "{amerFile}" to "{euroFileName}"...')
    shutil.move(amerFile, euroFileName)