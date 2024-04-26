from RPLCD.i2c import CharLCD
from bitcoin_value import currency
import time

# Init Display over i2c
lcd = CharLCD('PCF8574', 0x27)

# Setup Prompt for CLI
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
    # get current BTC price
    currentPrice = round(currency(fiat), 2)
    # calculate current portfolio value
    portfolioCurrent = round(currentPrice * float(coins), 2)
    # calculate current win or loss
    gainOrLoss = round(portfolioCurrent - portfolioCost, 2)
    roi = round(((portfolioCurrent - portfolioCost) / portfolioCost) * 100, 2)
    # Page 1
    lcd.write_string("BTC "+currentPrice)
    lcd.crlf()
    if gainOrLoss > 0:
        lcd.write_string("PROFIT "+gainOrLoss)
    else:
        lcd.write_string("LOSS "+gainOrLoss)
    # Page 2
    lcd.clear()
    lcd.write_string("VALUE "+portfolioCurrent)
    lcd.crlf()
    lcd.write_string("ROI "+roi)
    # Page 3
    lcd.clear()
    # add cpu temp
    time.sleep(10)