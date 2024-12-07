import requests

APP_ID = "c8dc8de4"
API_KEY = "3c0ca961dc88de7b8f587dfae44baa15"

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercises = input("Tell me which exercises you did: ")

exercises_params = {
    "query": exercises,
    "weight_kg": 74,
    "height_cm": 175,
    "age": 33
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercises_params, headers=headers)
print(response.json())