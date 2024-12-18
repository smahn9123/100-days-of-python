import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "208ab7d587ed10416141713ee5f85750"
MY_EMAIL = "secret"
MY_PASSWORD = "secret"

langitude = 36.830486
longitude = 127.145787

weather_params = {
    "lat": langitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # makes connection secure
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="secret",
            msg=f"Subject:It's going to rain today\n\nRemember to bring an umbrella!",
        )
