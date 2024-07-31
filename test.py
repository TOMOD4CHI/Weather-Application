import requests
import json
import time
city_name ='london'
api_key = 'cbe0235361316dba0bb43eaa292d7331'
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

response = requests.get(base_url)
data = response.json()
sunrise_time=time.localtime(data['sys']['sunrise'])
print(time.strftime("%H:%M", sunrise_time))