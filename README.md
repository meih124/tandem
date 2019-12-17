# Watering Schedule CLI app for Tandem SE Apprentice

## Instructions

#Goal: Create an application that generates a watering schedule for 12 weeks for plants.

Given: 'Apprentice_WeGrowInTandem_Data.json' contains data for plants.

Acceptance Criteria:
- The user can view which plant(s) to water on which date(s).
- The schedule covers the next 12 weeks starting Monday, 2019-12-16.
- No plants are watered on Saturdays or Sundays.
- Each plant is watered on its desired schedule as close as possible.


## Installation

Pre-conditions:
- Linux command line installed: macOS Terminal or Git BASH available here https://gitforwindows.org/
- Install Python 2.7 from https://www.python.org/downloads/
- Download the 2 files in this repo: 'Apprentice_WeGrowInTandem_Data.json' and 'json4.py' and place in working directory, e.g. for Windows '/c/Users/username'
- In Linux, be in the working directory, e.g. for Windows '/c/Users/username'


To run:
- In working directory, run command 'python json4.py'


## Extensions

- I formatted my stdout with 'dateTime' and 'summary' keys to add it to Google Calendar through their Python API. However, I was not able to figure out how to pass my Google Calendar EVENT details into the Google script.
- I tested 'json4.py' and noted that the standard Python errors would result if the filename was not found in the working directory or if I changed the start_date to a year out of range. Thus, I didn't add other ValueErrors to 'json4.py'.
- I tried to throw an error message if 'Apprentice_WeGrowInTandem_Data.json' is a blank file, but it didn't work.
- Also, I followed online instructions to be able to run 'python json4.py' in any directory, but it also didn't work.
