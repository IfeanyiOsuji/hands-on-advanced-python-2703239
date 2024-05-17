# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snowdays = list(filter(lambda d : d['snow'] > 0.0, weatherdata))
#print(len(snowdays))



# TODO: pretty-print the resulting data set
#pprint.pp(snowdays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summer_months = ['-07-', '-08-']
    if any(m in d['date'] for m in summer_months) and d['prcp'] >= 1.0:
        return True
    return False

summer_rain_days = list(filter(is_summer_rain_day, weatherdata))
##print(len(summer_rain_days))
pprint.pp(summer_rain_days)

def get_cold_windy_rainy_days():

    with open("../../sample-weather-history.json", "r") as weatherhistory:
        weatherdata = json.load(weatherhistory)
    pprint.pp(weatherdata)
    return list(filter(lambda x : x['prcp'] > 0.7 and ((x['tmax']+x['tmin'])/2 < 45) and x['awnd'] > 10.0, weatherdata))
    # your code goes here
pprint.pp(get_cold_windy_rainy_days())