from bitcoin_value import currency
import os
import time

# Clear screen for Mac and Linux
os.system("clear")

# Setup Prompt
print("Welcome to the 16x2 LCD BTC Tracker - By JetDev22")
print("-------------------------------------------------")
print("Before we begin, lets setup your portfolio:")
print("\n")
fiat = input("1. What fiat currency do you wish to use (EUR / USD)? ")
# Make input upper case
fiat = fiat.upper()
coins = input("2. How many BTC do you have? ")
cost = input("3. What was the average cost for your BTC? ")
print("-------------------------------------------------")
print(f"{coins} BTC at an average cost of {cost} {fiat}/BTC")
print("\n")
print("==> Your BTC LCD Tracker is now live :-)")
# Calculate base portfolio cost
portfolioCost = round(float(cost) * float(coins), 2)

# Main loop
while True:
    os.system("clear")
    print("Your Portfolio Data:")
    print("-------------------------------")
    # get current BTC price
    currentPrice = round(currency(fiat), 2)
    # calculate current portfolio value
    portfolioCurrent = round(currentPrice * float(coins), 2)
    # calculate current win or loss
    gainOrLoss = round(portfolioCurrent - portfolioCost, 2)
    roi = round(((portfolioCurrent - portfolioCost) / portfolioCost) * 100, 2)
    print(f"BTC = {currentPrice} {fiat}")
    if gainOrLoss > 0:
        print(f"Profit = {gainOrLoss} {fiat}")
    else:
        print(f"Loss = {gainOrLoss} {fiat}")
    print(f"Value = {portfolioCurrent} {fiat}")
    print(f"ROI = {roi} %")
    print("-------------------------------")
    time.sleep(10)