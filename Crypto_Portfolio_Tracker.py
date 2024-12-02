import requests
import time
from datetime import datetime
import pytz

portfolio = {
    'BTC': 0.01280118,
    
    }

def get_formatted_time():
    local_time_now = datetime.now(pytz.utc)
    return local_time_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

def get_crypto_price(ticker):
    url = f'https://api.coinbase.com/v2/prices/{ticker}-USD/spot'
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])

def display_portfolio(portfolio):
    print(f"----------------------------------------------------------\n")
    total_value = 0.0
    for ticker, amount in portfolio.items():
        formatted_time = get_formatted_time()
        price = get_crypto_price(ticker)
        value = amount * price
        total_value += value
        print(f"{ticker}: ${price:.2f} (You own {amount} {ticker}, Value: ${value:.2f})")
    print(f"{formatted_time} | Total Portfolio Value: ${total_value:.2f}\n")

def main():
    while True:
        display_portfolio(portfolio)
        time.sleep(10)

if __name__ == "__main__":
    main()