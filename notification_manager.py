import smtplib
import os

FROM_EMAIL = "lhltesting19@gmail.com"
FROM_PASSWORD = os.environ.get("FROM_PASSWORD")
TO_EMAIL = ADD_YOUR_EMAIL

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, search_data):
        self.price = search_data["price"]
        self.departure_city = search_data["cityFrom"]
        self.departure_airport_code = search_data["flyFrom"]
        self.arrival_city = search_data["cityTo"]
        self.arrival_airport_code = search_data["flyTo"]
        self.outbound_date = search_data["route"][0]["utc_departure"]
        self.inbound_date = search_data["route"][1]["utc_departure"]
        self.flight_link = search_data["deep_link"]

    def send_email_notification(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            body = f"Low price alert! Only ${self.price} to fly from \
{self.departure_city}-{self.departure_airport_code} to {self.arrival_city}-{self.arrival_airport_code}\
, from {self.outbound_date[0:10]} to {self.inbound_date[0:10]}.\nBook here: {self.flight_link}"
            connection.starttls()
            connection.login(user=FROM_EMAIL, password=FROM_PASSWORD)
            connection.sendmail(
                from_addr=FROM_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject: {self.arrival_city} Flight Deal!\n\n{body}"
            )

        print(f"Check your email for a {self.arrival_city} Flight Deal notification")
