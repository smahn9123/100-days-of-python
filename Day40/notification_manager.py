import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def send_notification(self, arrival_city, flight_data):
        price = flight_data.price
        departure_airport_code = flight_data.departure_airport_code
        arrival_airport_code = flight_data.arrival_airport_code
        departure_time = flight_data.departure_time
        arrival_time = flight_data.arrival_time

        message = (f"Flight from {departure_airport_code} to {arrival_airport_code} is for £{price}.\n"
                   f"Departure time: {departure_time}, Arrival time: {arrival_time}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("FROM_EMAIL"), password=os.getenv("FROM_EMAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.getenv("FROM_EMAIL"),
                to_addrs=os.getenv("TO_EMAIL"),
                msg=f"Subject:Lower Price found for flight from London to {arrival_city}!\n\n{message}".encode("utf-8"),
            )

    def send_emails(self, arrival_city, flight_data, users_email_list):
        price = flight_data.price
        departure_airport_code = flight_data.departure_airport_code
        number_of_stops = flight_data.number_of_stops
        arrival_airport_code = flight_data.arrival_airport_code
        departure_time = flight_data.departure_time
        arrival_time = flight_data.arrival_time

        message = (f"Flight from {departure_airport_code} to {arrival_airport_code} is for £{price}.\n"
                   f"Departure time: {departure_time}, Arrival time: {arrival_time}\n")

        if number_of_stops > 0:
            message += f"Number of stops: {number_of_stops}"

        for email in users_email_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=os.getenv("FROM_EMAIL"), password=os.getenv("FROM_EMAIL_PASSWORD"))
                connection.sendmail(
                    from_addr=os.getenv("FROM_EMAIL"),
                    to_addrs=email,
                    msg=f"Subject:Lower Price found for flight from London to {arrival_city}!\n\n{message}".encode("utf-8"),
                )
