import json

import sys
import requests

API = "https://api.coindesk.com/v1/bpi/currentprice.json"


def main():
    number_bc = validate_args_and_get_number()
    try:
        # Query the API for the CoinDesk Bitcoin Price
        response = requests.get(API)
        response_data = response.json()

        # Access current price of Bitcoin as a float
        rate = response_data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print("Request error!", e)
    except (ValueError, KeyError):
        print("Error parsing JSON or key not found!")

    amount = rate * number_bc

    # Outputs the current cost of Bitcoins in USD to four decimal places, using , as a thousands separator.
    print(f"${amount:,.4f}")


def validate_args_and_get_number():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            number_bc = float(sys.argv[1])
            # Give an error if number of bitcoins is a negative number
            if number_bc < 0:
                sys.exit("Error: Number of Bitcoins cannot be negative")
            return number_bc
        # If that argument cannot be converted to a float
        except ValueError:
            sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
