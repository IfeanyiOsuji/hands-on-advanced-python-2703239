# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
warmestDay = max(weatherdata, key=lambda x: x['tmax'])
print(f'Warmest date was {warmestDay["date"]} at temperature of {warmestDay["tmax"]} degree')

# TODO: What was the coldest day in the data set?
warmestDay = min(weatherdata, key=lambda x: x['tmin'])
print(f'Coldest date was {warmestDay["date"]} at temperature of {warmestDay["tmin"]} degree')

# TODO: How many days had snowfall?
snowday = [day for day in weatherdata if day['snow'] >0]
print(f'Snow fell on {len(snowday)} days')
