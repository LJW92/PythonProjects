from data_manager import DataManager, put_data
from flight_search import iata_code
from flight_data import FlightData
from notification_manager import notify_me

data = DataManager()
sheet_data = data.flight_data
flight_data = FlightData()


for item in sheet_data['prices']:
    if item['iataCode'] == '':
        iata_search = iata_code(item['city'])
        item['iataCode'] = iata_search
        put_data(item['id'], iata_search)

for item in sheet_data['prices']:
    cheapest_data = flight_data.cheap_flight_search(item['iataCode'])
    if cheapest_data[0] < item['lowestPrice']:
        message = f"Low price alert! Only £{cheapest_data[0]} " \
                  f"to fly from London-STN to {item['city']}-{item['iataCode']}, " \
                  f"from {cheapest_data[1]} to {cheapest_data[2]}."
        notify_me(message)
        break
