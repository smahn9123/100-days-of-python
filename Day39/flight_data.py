class FlightData:
    def __init__(self, price, arrival_city, departure_airport_code, arrival_airport_code, departure_time, arrival_time):
        self.price = price
        self.arrival_city = arrival_city
        self.departure_airport_code = departure_airport_code
        self.arrival_airport_code = arrival_airport_code
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    @staticmethod
    def find_cheapest_flight(arrival_city, flights_raw_data):
        if not flights_raw_data:
            return FlightData("N/A",
                              "N/A",
                              "N/A",
                              "N/A",
                              "N/A",
                              "N/A")

        first_price = float(flights_raw_data[0]["price"]["total"])
        first_departure_airport_code = flights_raw_data[0]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        first_arrival_airport_code = flights_raw_data[0]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        first_departure_time = flights_raw_data[0]["itineraries"][0]["segments"][0]["departure"]["at"]
        first_arrival_time = flights_raw_data[0]["itineraries"][0]["segments"][0]["arrival"]["at"]

        flight_data = FlightData(first_price,
                                 arrival_city,
                                 first_departure_airport_code,
                                 first_arrival_airport_code,
                                 first_departure_time,
                                 first_arrival_time)

        lowest_price = first_price

        for flight_raw_data in flights_raw_data[1:]:
            price = float(flight_raw_data["price"]["total"])
            if price < lowest_price:
                departure_airport_code = flight_raw_data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                arrival_airport_code = flight_raw_data["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                departure_time = flight_raw_data["itineraries"][0]["segments"][0]["departure"]["at"]
                arrival_time = flight_raw_data["itineraries"][0]["segments"][0]["arrival"]["at"]
                flight_data = FlightData(price,
                                         arrival_city,
                                         departure_airport_code,
                                         arrival_airport_code,
                                         departure_time,
                                         arrival_time)

        return flight_data
