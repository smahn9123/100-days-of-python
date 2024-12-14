import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class DataManager:
    def __init__(self):
        self.endpoint_prices = os.getenv("SHEETY_ENDPOINT_PRICES")
        self.endpoint_users = os.getenv("SHEETY_ENDPOINT_USERS")
        self.header = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }
        self.auth = HTTPBasicAuth(os.getenv("SHEETY_USERNAME"), os.getenv("SHEETY_PASSWORD"))

    def get_prices(self):
        response = requests.get(url=self.endpoint_prices, headers=self.header)
        return response.json()["prices"]

    def update_iata_code(self, iata_code, id):
        sheety_iata_code_params = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{self.endpoint_prices}/{id}", json=sheety_iata_code_params,
                                headers=self.header
                                # auth=self.auth
                                )
        return response.json()

    def get_customer_emails(self):
        response = requests.get(url=self.endpoint_users, headers=self.header)
        users_data = response.json()["users"]
        return [user_data["whatIsYourEmail?"] for user_data in users_data]
