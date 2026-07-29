import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    response.raise_for_status()
    data = response.json()
    price = float(data["data"]["priceUsd"])
except requests.RequestException:
    sys.exit("Request failed")

total = amount * price

print(f"${total:,.4f}")