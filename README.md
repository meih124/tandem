Watering Schedule CLI app for Tandem SE Apprentice

Pre-conditions:
- Linux command line installed: macOS Terminal or Git BASH available here https://gitforwindows.org/
- Install Python 2.7 from https://www.python.org/downloads/
- Download the 2 files in this repo: 'Apprentice_WeGrowInTandem_Data.json' and 'json4.py' and place in working directory, e.g. for Windows '/c/Users/username'
- In Linux, be in the working directory, e.g. for Windows '/c/Users/username'


To run:
- In working directory, run command 'python json4.py'


Extensions I would like to add:
- I formatted my stdout with 'dateTime' and 'summary' keys to add it to Google Calendar through their Python API. However, I was not able to figure out how to pass my Google Calendar EVENT details into the Google script.
- I tested my script 'json4.py' and noted that the standard Python errors would result if the filename was not found in the working directory or if I changed the start_date to a year out of range. Thus, I didn't add other ValueErrors to my script.
- Also, I tried to change the environment variable to be able to run 'python json4.py' in any directory, but it didn't work as I'd hoped.
