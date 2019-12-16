#!/usr/bin/env python
import json
import datetime
from datetime import date, timedelta


# Opens the json file with plant names and watering frequency
with open('Apprentice_WeGrowInTandem_Data.json') as f:
    data = json.load(f)


# Set start_date
start_date = datetime.date(2019, 12, 16)


# Loop through the json file
for ele in data:
    # Parse the integer from 'water_after' value
    x = int(ele['water_after'].split()[0])

    # Print the start_date for each plant
    print(dict(summary=ele['name'], dateTime=start_date.isoformat()))

    # Set current water date
    curr_date = start_date + timedelta(days=x)
    
    # Loop for 12 weeks from start_date inclusive of 12th Monday
    while curr_date < start_date + timedelta(days=7*12+1):
        # Condition if watering schedule lands on a weekend, +/- 1 day
        if curr_date.weekday() > 4:
            if curr_date.weekday() == 6:
                curr_date += timedelta(days=1)        
            elif curr_date.weekday() == 5:
                curr_date -= timedelta(days=1)
        # Print the current water date for that plant
        print(dict(summary=ele['name'], dateTime=curr_date.isoformat()))
        # Find the next water date for that plant
        curr_date += timedelta(days=x)
        
