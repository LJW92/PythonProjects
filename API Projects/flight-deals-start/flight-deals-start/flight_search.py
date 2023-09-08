import requests

API_KEY = 'lrQmCrdr_iZ01GYk7-FBPvrR7Vf2IFyI'

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

HEADER = {
    "apikey": API_KEY
}


def iata_code(city_name):
    input_params = {
        'term': city_name,
        'location_types': 'city',
    }
    response = requests.get(url=TEQUILA_ENDPOINT, params=input_params, headers=HEADER)
    response.raise_for_status()
    return response.json()['locations'][0]['code']


class FlightSearch:

    def __init__(self):
        pass
