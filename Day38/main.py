import requests
from datetime import datetime
import os

# APP_ID = "c8dc8de4"
# API_KEY = "3c0ca961dc88de7b8f587dfae44baa15"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# SHEETY_ENDPOINT = "https://api.sheety.co/a5c836dffe2451909aef5fff39e5d677/myWorkouts/workouts"
# SHEETY_BEARER_TOKEN = "Bearer toooken"

headers = {
    "x-app-id": os.environ["APP_ID"],
    "x-app-key": os.environ["API_KEY"],
}

exercises_params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": 74,
    "height_cm": 175,
    "age": 33
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercises_params, headers=headers)
data = response.json()

sheety_header = {
    "Authorization": os.environ["SHEETY_BEARER_TOKEN"],
}

for exercise in data["exercises"]:
    sheety_params = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=os.environ["SHEETY_ENDPOINT"], json=sheety_params, headers=sheety_header)
    data = sheety_response.json()
    print(data)
