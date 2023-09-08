import requests
from datetime import datetime
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# response_json = response.json()
# print(response_json)
# longitude_ = response_json['iss_position']['longitude']
# latitude = response_json['iss_position']['latitude']
MY_LAT = -35.280937
MY_LNG = 149.130005
API = 'https://api.sunrise-sunset.org/json'
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}
response = requests.get(API, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

sunrise_time = (int(sunrise.split('T')[1].split(':')[0]) + 10) % 24
sunset_time = (int(sunset.split('T')[1].split(':')[0]) + 10) % 24
print(sunrise_time)
print(sunset_time)
time_now = datetime.now()
print(time_now)

