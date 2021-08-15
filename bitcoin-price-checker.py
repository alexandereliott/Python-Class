
# Bitcoin Price Checker.

"""# This script will send a request out to bitfinex and request information in the form of json and then the script will compare the information it has received to the set parametered in the code will either send an alert if the price has went past a certain threshold or will cancel and wait a certain amount of time and check again."""

import requests
import json


# The script import requests and json.

r = requests.get('https://api.bitfinex.com/v1/ticker/btcusd')

# The script scraps the bitfinex API for the latest bitcoin prices.

print(r.text)

# The script prints ouf the scraped json information that it acquired.



s = json.loads('{"mid":"47205.5","bid":"47205.0","ask":"47206.0","last_price":"47206.0","timestamp":"1628990307.005424163"}')

print(s["mid"])








