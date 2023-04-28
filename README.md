# Flight Deals Project

## What does it do?
You can have great round trip flight deals to your dream destinations emailed to you. It does all the searching for you! 

In this [google sheet](https://docs.google.com/spreadsheets/d/1UtL1nK5DA0_wql6Hjl-1kQs4ulSJ1-FB3VJ0nxBlqbE/edit?usp=sharing), you can list the names of cities you'd like to travel to in cloumn A and the highest price you'd be willing to pay for a round trip flight there in column C. Then when the program is run it will fill in the [IATA Code](https://en.wikipedia.org/wiki/IATA_airport_code) for each location and search for flight deals on kiwi.com. If a flight is found for under your price point it will send an email to you, containing the flight information and a link to book your flight.

## How to run it
1. Download this project
2. In notification_manager.py replace the `ADD_EMAIL` placeholder with your personal email; It must be a gmail account.
3. Run `main.py`
4. Enjoy! 

## Considerations
The free version of the [Sheety API](https://sheety.co/) only allows 200 requests a month before asking you to upgrade. Create a free account, make a copy of the above google sheet and insert your own `SHEETY_ENDPOINT` in data_manager.py instead if desired. 
