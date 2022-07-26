#! python3
# getOpenWeather.py - Prints the weather for a location from the command line

import json, sys
from urllib import response
import requests

APPID = 'your_key'

if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s' % (location,APPID)
print(url)
response = requests.get(url)
response.raise_for_status
print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)
# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])