import datetime as dt
import pandas
import smtplib
import random

MY_EMAIL = "secret"
MY_PASSWORD = "secret"

today = dt.datetime.today()
data = pandas.read_csv("birthdays.csv")
today_is_birthday = data[(data.month == today.month) & (data.day == today.day)][["name", "email"]]

birthdays_dict_list = today_is_birthday.to_dict(orient="records")
if len(birthdays_dict_list) > 0:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        letter_content = letter_file.read()

    for item in birthdays_dict_list:
        name = item['name']
        email = item['email']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # makes connection secure
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{letter_content.replace("[NAME]", name)}",
            )
