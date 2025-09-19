# Hardcoded stock prices
stock_prices = {
    "KTM": 500090,
    "BMW": 800000,
    "MT": 255050,
    "DUCATI": 844000,
    "HONDA": 300000
}

# Get user input for stock names and quantities
stocks = {}
while True:
    name = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if name == 'DONE':
        break
    if name in stock_prices:
        qty = int(input(f"Enter quantity for {name}: "))
        stocks[name] = qty
    else:
        print("Stock not found in the price list.")

# Calculate total investment
total = 0
for stock, qty in stocks.items():
    total += stock_prices[stock] * qty

print(f"Total investment: {total}")