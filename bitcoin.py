import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit(1)
else:
    bit_dict = response.json()
    bit_price = bit_dict["bpi"]["USD"]["rate_float"]
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else: 
    try:
        user_input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        print(f"${user_input * bit_price:,.4f}")