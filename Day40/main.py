from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_prices()
# print(sheet_data)

flight_search = FlightSearch()

for city in sheet_data:
    if not city["iataCode"]:
        city["iataCode"] =  flight_search.get_iata_code(city["city"])

print(sheet_data)

# for city in sheet_data:
#     data_manager.update_iata_code(city["iataCode"], city["id"])

notification_manager = NotificationManager()

for city in sheet_data:
    flights_raw_data = flight_search.get_flights_raw_data(city)
    flight_data = FlightData.find_cheapest_flight(city["city"], flights_raw_data)
    # print(flight_data)

    if flight_data.price == "N/A":
        print(f"No flight to {city['city']} for next 6 months found.")
    elif flight_data.price < city["lowestPrice"]:
        print(f"Lower price found for flight to {city['city']}! £{flight_data.price}")
        notification_manager.send_notification(city["city"], flight_data)
    else:
        print(f"Lower price for flight to {city['city']} not found.")
