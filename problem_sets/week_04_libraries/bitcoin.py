# command line argument the number of bitcoins, n, that they want to buy
# if it can't be converted to a float, exit the program via sys.exit with error msg
# query coindesk API for BTC price at https://api.coindesk.com/v1/bpi/currentprice.json
# nested keys is the price of BTC as a float
# catch any exceptions
# requests module for `get` method


# By separating the code into functions, it improves modularity, readability, and reusability. The main() function serves as the entry point of the program, and the functions get_btc_amount() and get_btc_price() handle specific tasks
import sys, requests


# executing the main logic of the program. It calls the get_btc_amount() and get_btc_price() functions to obtain the BTC amount and price, calculates the total cost, formats the output, and displays the result to the user
def main():
    btc_amount = get_btc_amount()
    btc_price = get_btc_price()
    total_btc_cost = btc_amount * btc_price
    formatted_total_btc_cost = f"${total_btc_cost:,.4f}"

    print(formatted_total_btc_cost)


# checks the command-line argument, extracts the BTC amount, and returns it as a float value. It handles any potential errors related to the command-line argument.
def get_btc_amount():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    return n


# makes the API request to obtain the BTC price from the CoinDesk API. It handles exceptions related to the API request and response, extracts the price from the JSON data, and returns it as a float value
def get_btc_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        print("Request error")
        sys.exit(1)

    return price


if __name__ == "__main__":
    main()
