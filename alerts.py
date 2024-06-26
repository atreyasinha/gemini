"""
Module generates alerts for each of the symbols that Gemini 
trades if the standard deviation from the hourly prices
for past 24 hours is more than 1
"""
import json
import statistics
import datetime
import requests


def get_traded_symbols():
    """
    Function to get a list of traded symbols from the Gemini API
    Send a GET request to the Gemini API to retrieve the list of symbols
    Return the list of symbols in JSON format
    """
    response = requests.get("https://api.gemini.com/v1/symbols")
    return response.json()


def get_prices(symbol):
    """
    Function to get historical price data for a given symbol
    Send a GET request to the Gemini API to retrieve the historical price data
    Extract the closing prices from the response
    """
    response = requests.get(f"https://api.gemini.com/v2/candles/{symbol}/1m")
    closing_price = []
    for p in response.json():
        closing_price.append(p[4])

    return closing_price


def generate_alert(symbol, deviation, last_price, average_price, price_change):
    """
    Function to generate an alert based on price deviation
    Create a dictionary to store the alert data
    Print the alert data in JSON format
    """
    alert = {
        "timestamp": datetime.datetime.now().isoformat(),   # Current timestamp
        "log_level": "P4",                                  # Log level of the alert
        "trading_pair": symbol,                             # Symbol of the trading pair
        # True if the deviation is greater than 1
        "deviation": deviation > 1,
        "data": {
            "last_price": last_price,                       # Last price of the symbol
            "average_price": average_price,                 # Average price of the symbol
            "deviation": deviation,                         # Deviation of the symbol
            "price_change_value": price_change              # Price change of the symbol
        }
    }

    print(json.dumps(alert))


def main():
    """Main function to process the symbols and generate alerts"""
    symbols = get_traded_symbols()

    for symbol in symbols:
        try:
            # Get the historical price data for the symbol
            prices = get_prices(symbol)
            # Calculate the average price and deviation
            average_price = statistics.mean(prices)
            deviation = statistics.stdev(prices)
            # Get the last price and calculate the price change
            last_price = prices[0]
            price_change = last_price - average_price
            # Generate an alert based on the price deviation
            generate_alert(symbol, deviation, last_price,
                           average_price, price_change)
        except Exception as e:  # pylint: disable=broad-exception-caught
            # Print an error message if an exception occurs
            print(f"Error processing {symbol}: {str(e)}")


# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
