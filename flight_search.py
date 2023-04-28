import requests
import os

FLIGHT_LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.flight_city = city

    def get_iatta_code(self):
        location_header = {
            "apiKey": KIWI_API_KEY
        }

        location_params = {
            "term": self.flight_city,
            "location_types": "city"
        }
        response = requests.get(url=FLIGHT_LOCATION_ENDPOINT, headers=location_header, params=location_params)
        flight_data = response.json()
        iatta_code = flight_data['locations'][0]['code']
        return iatta_code

