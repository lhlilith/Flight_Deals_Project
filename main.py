from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

google_sheet = DataManager()
sheet_data = google_sheet.get_sheet_data()

for row in sheet_data:
    flight = FlightSearch(row['city'])
    row_id = row['id']
    row['iataCode'] = flight.get_iatta_code()
    exclude_key = ['id']
    row_contents = {key: row[key] for key in set(list(row.keys())) - set(exclude_key)}
    google_sheet.update_iatacode(row_id, row_contents)
    flight_data = FlightData(row)
    flight_price, search_data = flight_data.find_flight_price()

    if flight_price < row['lowestPrice'] and flight_price > 0:
        print("Preparing notification to send...")
        notification_info = NotificationManager(search_data["data"][0])
        notification_info.send_sms_notification()
