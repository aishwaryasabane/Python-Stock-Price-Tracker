import requests
import json
import tkinter as tk
import config
from tkinter import Label, StringVar

ALPHA_VANTAGE_API_KEY = config.api_key
SYMBOL = 'AAPL'

def get_stock_price(api_key, symbol):
    base_url = 'https://www.alphavantage.co/query'
    function = 'GLOBAL_QUOTE'

    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        print(data)
        if 'Global Quote' in data:
            return data['Global Quote']['05. price']
        else:
            return None

    except requests.RequestException as e:
        print(f"Error fetching stock price: {e}")
        return None

def update_stock_price():
    stock_price = get_stock_price(ALPHA_VANTAGE_API_KEY, SYMBOL)

    if stock_price:
        result.set(f"Stock Price ({SYMBOL}): ${stock_price}")
    else:
        result.set("Error fetching stock price")

    # Schedule the next update after 5 seconds
    root.after(5000, update_stock_price)

# Create the main window
root = tk.Tk()
root.title("Stock Price Tracker")

# Variable to store the stock price
result = StringVar()

# Label to display the stock price
label = Label(root, textvariable=result, font=('Helvetica', 14))
label.pack(pady=20)

# Button to manually update the stock price
update_button = tk.Button(root, text="Update Price", command=update_stock_price)
update_button.pack()

# Initial update
update_stock_price()

# Start the Tkinter main loop
root.mainloop()
