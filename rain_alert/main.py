import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "your api key"
account_sid = "your sid"
auth_token = "your token"

parameters = {
    'lat': -35.280937,
    'lon': 149.130005,
    'appid': api_key,
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
id_data = weather_data['weather'][0]['id']

if id_data < 700:
    print("Bring an umbrella")

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="It's going to rain today. Remember to bring an umbrella ☂️",
    from_="+12512374840",
    to='+61450180802'
)
print(message.status)