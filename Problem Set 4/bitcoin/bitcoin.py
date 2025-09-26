import sys
import requests
import json

# Expects the user to specify as a command-line argument the number of Bitcoins
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too Many arguments")

try:
    converted = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


# Api call and conversion
try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    response.raise_for_status()

    o = response.json()  # Use json() to be readable
    rate = o["data"][
        "priceUsd"
    ]  # Indexing directly into the dictonary and it's value. Taught by https://youtu.be/SMgs44aqeLw?si=C901hgLXdELxrh4a
    rate = float(rate)

    print(
        f"Amount in dollars is ${rate * converted:,.4f}"
    )  # Format to four decimal places with a thousand separator using ':,.4f' . Link: https://docs.python.org/3/library/string.html#formatspec

# Error to watch out for:
except requests.RequestException as e:
    print(f"Request error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
