
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 310
}

portfolio = {}

num_stocks = int(input("Enter number of different stocks you want to add: "))

for i in range(num_stocks):
    stock = input(f"Enter stock {i+1} name: ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print(f" Warning: {stock} is not in our price list and will be skipped.")

total_investment = 0
print("\nYour Portfolio Details:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"- {stock}: {quantity} shares at ${price} each = ${value}")

print(f"\n Total investment value: ${total_investment}")

save_option = input("Do you want to save this to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares at ${price} each = ${value}\n")
        file.write(f"\nTotal investment: ${total_investment}\n")
    print(" Portfolio saved to 'portfolio_summary.txt'.")
