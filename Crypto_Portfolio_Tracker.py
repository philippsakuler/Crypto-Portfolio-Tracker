import requests
import time
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

#Specifies crypto holdings
portfolio = {
    'BTC': 0.01280118,
    'ETH': 0.4,
    
    }

#Stores portfolio history
portfolio_history = {
    'timestamps': [],
    'values': [],
    'individual_values': {ticker: [] for ticker in portfolio},
    }

#Fetches current UTC time
def get_formatted_time():
    local_time_now = datetime.now(pytz.utc)
    return local_time_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

#Fetches the latest cryptocurrency price in USD using Coinbase's API
def get_crypto_price(ticker):
    url = f'https://api.coinbase.com/v2/prices/{ticker}-USD/spot'
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])

#Displays portfolio
def display_portfolio(portfolio):
    print(f"----------------------------------------------------------\n")
    total_value = 0.0
    prices = {}  #Stores prices to avoid redundant API calls
    
    for ticker, amount in portfolio.items():
        price = get_crypto_price(ticker)
        prices[ticker] = price  #Saves fetched price
        value = amount * price
        total_value += value
        print(f"{ticker}: ${price:.2f} (You own {amount} {ticker}, Value: ${value:.2f})")
    
    print(f"{get_formatted_time()} | Total Portfolio Value: ${total_value:.2f}\n")
    
    #Passes prices to update_portfolio_history
    update_portfolio_history(portfolio, prices)

#Updates portfolio history
def update_portfolio_history(portfolio, prices):
    total_value = 0.0
    for ticker, amount in portfolio.items():
        price = prices[ticker]  #Uses pre-fetched price
        value = amount * price
        total_value += value

        #Appends individual value
        portfolio_history['individual_values'][ticker].append(value)

    #Appends total portfolio value
    portfolio_history['timestamps'].append(get_formatted_time())
    portfolio_history['values'].append(total_value)

    print(f"Total Portfolio Value Updated: ${total_value:.2f}")

#Visualizes portfolio
def plot_portfolio():
    plt.figure(1, figsize=(10, 5))  # Use figure number 1 to reuse the same window
    plt.clf()  #Clears the existing plot

    #Ensures there is data to plot
    if not portfolio_history['timestamps'] or not portfolio_history['values']:
        print("No data to plot yet.")
        return

    #Pie chart for distribution
    latest_values = {ticker: portfolio_history['individual_values'][ticker][-1] for ticker in portfolio}
    
    #Pie chart
    plt.subplot(1, 2, 1)
    plt.pie(latest_values.values(), labels=latest_values.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Portfolio Distribution')
    
    
    #Line chart for portfolio value over time
    plt.subplot(1, 2, 2)
    plt.plot(portfolio_history['timestamps'], portfolio_history['values'], label='Total Portfolio Value')
    
    #Formats x-axis labels to show only time
    short_timestamps = [ts.split(' ')[1][:5] for ts in portfolio_history['timestamps']]
    tick_positions = range(len(short_timestamps))  # Create a range for the ticks

    plt.gca().set_xticks(tick_positions)  # Set explicit tick positions
    plt.gca().set_xticklabels(short_timestamps, rotation=90, ha='right')  # Set labels
    
    
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value ($)')
    plt.title('Portfolio Value Over Time')
    plt.legend()

    plt.tight_layout()
    plt.pause(0.1)  #Allows the script to continue execution

#Update loop
def main():
    while True:
        display_portfolio(portfolio)
        plot_portfolio()
        time.sleep(2)

if __name__ == "__main__":
    main()