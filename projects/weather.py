import requests
import json
import os

city = input('Enter city name: ')
# url = f'https://api.weatherapi.com'

# r = requests.get(url)
# dic = json.loads(r.text)

# temp = dic['current'['temp_c']]
temp = 56

command = f'espeak "The current temperature of {city} is {temp} degrees" '
os.system(command)