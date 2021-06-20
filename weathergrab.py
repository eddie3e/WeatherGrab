import requests
import json
import sys
import re
from datetime import datetime

## Select from data file keys [daily][temp][min],[max]


api_key = "00f1cd75fbc170f7c600dd35862a33d3"
## currnet home location
lat = "42.254931"
lon = "-70.8983301"

## try to take user input to grab region loaction
user_request = input("Please enter your zip code:\n")
r = re.search("[5]", user_request)

print(r)

## request using Imperial, not standard (k) or metric (c)
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" %(lat, lon, api_key)

## use response libarry to grab data from openweather.org
response = requests.get(url)

## create json object as dict?
weather_json = response.json()

## retrieve a nested dict and print as example
temp = weather_json['current']['temp']
print(temp)

##put data into string to print or something else
data = json.loads(response.text)

##print(data)
date_today = datetime.now()
format = "%d%m%Y%H%M%S"
time1 = date_today.strftime(format)

print(time1)
todaysfile = 'datafile'+time1+'.txt'
print(todaysfile)

## print to file using json dump function using text
f = open('{}.txt'.format(todaysfile), 'w')
json.dump(data, f)
f.close()

##with open('data_file.txt') as f:
  ##  json.dump(data, f)
    
