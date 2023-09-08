import requests

SHEET_ENDPOINT = "https://api.sheety.co/791b9114d181bc5cbb671905412a4c52/flightDeals/prices"

SHEET_HEADER = {
    'Authorization': 'Bearer 349267842',
}


def put_data(data_id, iata_code):
    input_data = {
        "price": {
            "iataCode": iata_code,
        }
    }
    response = requests.put(url=f"{SHEET_ENDPOINT}/{data_id}", json=input_data, headers=SHEET_HEADER)
    response.raise_for_status()
    print(response.text)


class DataManager:

    def __init__(self):
        self.flight_data = {}
        self.refresh_data()

    def refresh_data(self):
        response = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADER)
        response.raise_for_status()
        self.flight_data = response.json()
