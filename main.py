# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from flight_search import FlightSearch
from notification_manager import NotificationManager
from data_manager import DataManager
from datetime import *
from dateutil.relativedelta import *

data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()

date_from = datetime.now() + timedelta(days=1)
date_to = datetime.now() + relativedelta(months=6)
FLY_FROM = "CEB"

sheet_data = data_manager.get_data()

for data in sheet_data:
    iata_code = data["iataCode"]
    if iata_code == "":
        iata_code = flight_search.get_IATA(data['city'])
        data_manager.update_iata(iata_code, data["id"])


for data in sheet_data:
    flight = flight_search.search_flights(
        data["iataCode"],
        FLY_FROM,
        date_from,
        date_to
    )

    # if flight is not None:
    #     print(flight.price, data["lowestPrice"])
    if flight is not None and flight.price < data["lowestPrice"]:
        notification_manager.send_mail(flight)