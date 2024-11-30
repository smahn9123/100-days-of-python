import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 36.815029 # Your latitude
MY_LONG = 127.114067 # Your longitude

MY_EMAIL = "xxx@gmail.com"
MY_PASSWORD = "secret"

def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    return abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = (sunrise + 9) % 24 # [BUG] returned value has 9-hour difference
    sunset = (sunset + 9) % 24 # [BUG]returned value has 9-hour difference

    time_now = datetime.now()
    return time_now.hour < sunrise or sunset <= time_now.hour

while True:
    if is_iss_close() and is_dark():
        print("ISS is close - Sending Email!")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="yyy@yahoo.com",
                msg=f"Subject:Look at the sky\n\nISS is up in the sky!",
            )
    time.sleep(60)
