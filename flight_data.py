import datetime as dt
import requests
from flight_search import KIWI_API_KEY

FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, row):
        self.departure_city = row['city']
        self.departure_airport_code = row['iataCode']
        self.price = row['lowestPrice']

    def find_flight_price(self):
        today = dt.date.today()
        tomorrow = today + dt.timedelta(days=1)
        six_months_from_today = today + dt.timedelta(days=180)
        week_from_today = today + dt.timedelta(days=7)
        month_days_from_today = today + dt.timedelta(days=28)
        # search price of flight from BOS to city
        search_header = {
            "apiKey": KIWI_API_KEY
        }
        search_params = {
            "fly_from": "BOS",
            "fly_to": self.departure_airport_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": six_months_from_today.strftime("%d/%m/%Y"),
            "return_from": week_from_today.strftime("%d/%m/%Y"),
            "return_to": month_days_from_today.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "max_stopovers": "0",
            "curr": "USD"
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=search_header, params=search_params)
        search_data = response.json()
        if len(search_data["data"]) > 0:
            flight_price = search_data["data"][0]["price"]
        else:
            flight_price = 0
        return flight_price, search_data
