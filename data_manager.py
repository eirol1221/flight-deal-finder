import requests
from pprint import pprint
import os

SHEETY_URL = os.environ["SHEETY_URL"]

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def get_data(self):
        response = requests.get(url=SHEETY_URL)
        return response.json()['prices']

    def update_iata(self, iata_code, id):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }

        response = requests.put(url=f"{SHEETY_URL}/{id}",
                                json=body)
        print(response.text)