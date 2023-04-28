import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c68e6dcf4fba7a501340f86601c4f373/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet
    def __init__(self):
        self.flight_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.flight_data = data['prices']
        return self.flight_data

    def update_iatacode(self, row_id, row_contents):
        changes = {
            "price": row_contents
        }
        requests.put(url=f"{SHEETY_ENDPOINT}/{row_id}", json=changes)
