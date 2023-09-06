import smtplib
from datetime import datetime

import requests

MY_LAT = -35.280937
MY_LONG = 149.130005
my_email = 'lijiaweipython@gmail.com'
password = 'ajnqjljoqbhfhcuu'

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) % 24
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) % 24

time_now = datetime.now()

if iss_latitude > MY_LAT - 5 and iss_longitude < MY_LAT + 5 \
        and iss_latitude > MY_LONG - 5 and iss_longitude < MY_LONG + 5 and time_now not in range(sunrise, sunset):
    with smtplib.SMTP('smtp.gmail.com') as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        connect.sendmail(from_addr=my_email,
                         to_addrs='lijiaweipython@yahoo.com',
                         msg=f'Subject:Look up\n\n iss on above'
                         )

# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
