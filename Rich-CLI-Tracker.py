from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.markdown import Markdown
from rich.console import Console
from bitcoin_value import currency
import os
import time

console = Console()

# Markdown Texts
titleBig = Markdown("""# BTC TRACKER""")
welcome = Markdown("""# WELCOME TO CLI BTC TRACKER - by JetDev22""")

# BTC Symbol
btcLogo = u"\u20BF"

# Setup Prompt
os.system("clear")
console.print(welcome)
print("Before we begin, lets setup your portfolio:")
print("-----------------------------------------------------------")
fiat = input("1. What fiat currency do you wish to use (EUR / USD)? ")
fiat = fiat.upper()
coins = input("2. How many BTC do you have? ")
cost = input("3. What was the average cost for your BTC? ")
print("---- Optional: Leave blank if not needed ----")
dca = input("4. What is your dollar cost average amount? ")

# Set FIAT symbol
fiatSymbol = ""
if fiat == "EUR":
    fiatSymbol = "€"
else:
    fiatSymbol = "$"

# Calculate Portfolio Cost
portfolioCost = round(float(cost) * float(coins), 2)

# Return cost of portfolio
print("-----------------------------------------------------------")
print(f"          Your {btcLogo} Portfolio cost you {portfolioCost} {fiatSymbol}")
print("-----------------------------------------------------------")

# Progressbar to allow to read portfolio value
for i in track(range(5), description="Switchig to BTC Tracker ", complete_style="green"):
    time.sleep(1)

# Markdown Texts
titleBig = Markdown("""# BTC TRACKER""")

# Main Loop
while True:
    os.system("clear")
    # get current BTC price
    currentPrice = round(currency(fiat), 2)
    # calculate current portfolio value
    portfolioCurrent = round(currentPrice * float(coins), 2)
    # calculate current win or loss
    gainOrLoss = round(portfolioCurrent - portfolioCost, 2)
    roi = round(((portfolioCurrent - portfolioCost) / portfolioCost) * 100, 2)
    # Generate Table 
    table = Table(show_header=True, header_style="bold yellow", title_justify="center", width=68, title=titleBig)
    # Generate Columns
    table.add_column("DATAPOINT", justify="left", style="bold")
    if gainOrLoss > 0:
        table.add_column("RESULT", justify="right", style="green")
    else:
        table.add_column("RESULT", justify="center", style="red")
    table.add_column("UNIT", justify="center", style="bold")
    # Generate Rows
    table.add_row("CURRENT BTC PRICE", str(currentPrice), fiatSymbol)
    table.add_row("COINS HELD", str(coins), btcLogo)
    # Check if Profit or loss
    if gainOrLoss > 0:
        table.add_row("PROFIT", str(gainOrLoss), fiatSymbol)
    else:
        table.add_row("LOSS", str(gainOrLoss), fiatSymbol)
    table.add_row("RETURN OF INVESTMENT", str(roi), "%")
    # Check if dca amount given
    if len(dca) != 0:
        dcaFloat = float(dca)
        dcaBTC = round(dcaFloat / currentPrice, 5)
        annualDCA = round(dcaFloat * 12, 2)
        table.add_row(dca+" "+fiatSymbol+ " DCA AMOUNTS TO", str(dcaBTC), btcLogo)
        table.add_row("DCA / YEAR", str(annualDCA), fiatSymbol)
    # Print Table
    console.print(table)
    print("")
    # Progress-Bar
    for i in track(range(20), description="Refreshing in", complete_style="green"):
        time.sleep(1)