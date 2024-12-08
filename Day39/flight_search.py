import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        return response.json()["access_token"]

    def get_iata_code(self, city):
        header = {
            "Authorization": "Bearer " + self._token,
        }
        amadeus_iata_code_params = {
            "keyword": city,
        }
        response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
                                headers=header,
                                params=amadeus_iata_code_params
                                )
        try:
            return response.json()["data"][0]["iataCode"]
        except IndexError:
            return "N/A"
        except KeyError:
            return "N/A"

    def get_flights_raw_data(self, city):
        header = {
            "Authorization": "Bearer " + self._token,
        }
        print(f"Getting flights for {city['city']}...")

        flights = []
        day = datetime.today() + timedelta(days=1)
        while day <= datetime.today() + timedelta(days=3):
            amadeus_flight_offers_params = {
                "originLocationCode": "LON",
                "destinationLocationCode": city["iataCode"],
                "departureDate": day.strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP",
            }
            response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers",
                                    headers=header,
                                    params=amadeus_flight_offers_params
                                    )
            flights.extend(response.json()["data"])

            day += timedelta(days=1)

        return flights