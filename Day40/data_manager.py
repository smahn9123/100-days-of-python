import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.endpoint = os.getenv("SHEETY_ENDPOINT")
        self.header = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }
        self.auth = HTTPBasicAuth(os.getenv("SHEETY_USERNAME"), os.getenv("SHEETY_PASSWORD"))

    def get_prices(self):
        response = requests.get(url=self.endpoint, headers=self.header)
        return response.json()["prices"]

    def update_iata_code(self, iata_code, id):
        sheety_iata_code_params = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.endpoint}/{id}", json=sheety_iata_code_params,
                                headers=self.header
                                # auth=self.auth
                                )
        return response.json()
