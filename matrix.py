import time
import sys
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from bitcoin_value import currency
from rich.markdown import Markdown
from rich.console import Console

# Matrix Conf
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.brightness = 70
options.chain_length = 1
options.disable_hardware_pulsing = 1
options.hardware_mapping = 'regular'
matrix = RGBMatrix(options = options)

# Load Canvas and Font
matrixScreen = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("/home/wotan/rpi-rgb-led-matrix/fonts/6x10.bdf")
pos = matrix.height

# Setup Prompt
console = Console()
os.system("clear")
console.print(Markdown("""# WELCOME TO CLI BTC TRACKER - by JetDev22"""))
print("Before we begin, lets setup your portfolio:")
print("-----------------------------------------------------------")
fiat = input("1. What fiat currency do you wish to use (EUR / USD)? ")
fiat = fiat.upper()
coins = input("2. How many BTC do you have? ")
cost = input("3. What was the average cost for your BTC? ")
print("---- Optional: Leave blank if not needed ----")
dca = input("4. What is your dollar cost average amount? ")
#predictions = input("5. Display portfolio 'what if' predictions (Y/N)? ")

# Set FIAT symbol
if fiat == "EUR":
    fiatSymbol = "€"
    
# BTC Symbol
btcLogo = u"\u20BF"

# Calculate Portfolio Cost
portfolioCost = round(float(cost) * float(coins), 2)

# Return cost of portfolio
print("-----------------------------------------------------------")
print(f"          Your {btcLogo} Portfolio cost you {portfolioCost} {fiatSymbol}")
print("-----------------------------------------------------------")
console.print(Markdown("""# Led Matrix starting"""))


# Main Loop
while True:
    matrix.Clear()
    matrixScreen.Clear()
    pos_x=0
    pos_y=font.height
    color_R=255
    color_G=255
    color_B=255


    while True:
        # Load current BTC Price
        currentPrice = round(currency(fiat), 2)
        # Calculations
        portfolioCurrent = round(currentPrice * float(coins), 2)
        gainOrLoss = round(portfolioCurrent - portfolioCost, 2)
        roi = round(((portfolioCurrent - portfolioCost) / portfolioCost) * 100, 2)
        # Draw 1st Page
        line0 = graphics.DrawText(matrixScreen, font,1, pos_y,graphics.Color(255,255,100),"BTC")
        line1 = graphics.DrawText(matrixScreen, font,1, 20,graphics.Color(color_R,color_G,color_B),str(currentPrice))
        line2 = graphics.DrawText(matrixScreen, font,1, 25,graphics.Color(color_R,color_G,color_B),"----------")
        line3 = graphics.DrawText(matrixScreen, font,1, 30,graphics.Color(255,255,100),"COINS")
        line4 = graphics.DrawText(matrixScreen, font,1, 40,graphics.Color(color_R,color_G,color_B),str(coins))
        line5 = graphics.DrawText(matrixScreen, font,1, 45,graphics.Color(color_R,color_G,color_B),"----------")
        line6 = graphics.DrawText(matrixScreen, font,1, 50,graphics.Color(255,255,100),"PROFIT")
        if gainOrLoss > 0:
            line7 = graphics.DrawText(matrixScreen, font,1, 60,graphics.Color(000,255,000),str(gainOrLoss))
        else:
            line7 = graphics.DrawText(matrixScreen, font,1, 60,graphics.Color(255,000,000),str(gainOrLoss))
        time.sleep(5)
        matrixScreen = matrix.SwapOnVSync(matrixScreen)
        matrixScreen.Clear()