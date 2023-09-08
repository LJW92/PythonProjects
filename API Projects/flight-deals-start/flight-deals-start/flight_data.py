import datetime as dt
import requests

from flight_search import HEADER

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightData:

    def __init__(self):
        self.now = dt.datetime.now()
        self.from_date = self.now + dt.timedelta(days=1)
        self.to_date = self.now + dt.timedelta(days=180)

    def cheap_flight_search(self, fly_to: str):
        input_data = {
            'fly_from': 'LON',
            'fly_to': fly_to,
            'date_from': self.from_date.strftime('%d/%m/%Y'),
            'date_to': self.to_date.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'max_stopovers': 0,
            'curr': 'GBP',
            'limit': 1
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=input_data, headers=HEADER)
        response.raise_for_status()
        data_string = response.json()['data'][0]
        return [data_string['price'],
                data_string['local_departure'].split('T')[0],
                data_string['route'][1]['local_arrival'].split('T')[0]]

