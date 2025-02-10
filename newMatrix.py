import time
import os
import sys
import requests
from PIL import Image
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from bitcoin_value import currency
from rich.markdown import Markdown
from rich.console import Console
from gpiozero import CPUTemperature

# Matrix Conf
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.brightness = 40
options.chain_length = 1
options.disable_hardware_pulsing = 0
options.hardware_mapping = 'regular'
options.gpio_slowdown = 4
matrix = RGBMatrix(options = options)

# Load Canvas and Font
matrixScreen = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("/home/wotan/rpi-rgb-led-matrix/fonts/MatrixChunky8.bdf")
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
else:
    fiatSymbol = "$"

# BTC Symbol
btcLogo = u"\u20BF"


# Calculate Portfolio Cost
portfolioCost = round(float(cost) * float(coins), 2)

# Return cost of portfolio
print("-----------------------------------------------------------")
print(f"          Your {btcLogo} Portfolio cost you {portfolioCost} {fiatSymbol}")
print("-----------------------------------------------------------")
console.print(Markdown("""# LED-Matrix starting"""))

# LOGIC
def getCpuTemp():
    cpu = CPUTemperature()
    cpuTemp = round(cpu.temperature, 2)

def loadImage(image):
    background = Image.open(image)
    matrix.SetImage(background.convert('RGB'))

# Main Loop
while True:
    try:
        #currentPrice = round(currency(fiat), 2)
        response = requests.get("https://blockchain.info/ticker")
        data = response.json()
        currentPrice = float(data[fiat]["last"])
    except requests.exceptions.RequestException as e:
        print("BTC Price request failed", e)
        currentPrice = 50000
    portfolioCurrent = round(currentPrice * float(coins), 2)
    gainOrLoss = round(portfolioCurrent - portfolioCost, 2)
    roi = round(((portfolioCurrent - portfolioCost) / portfolioCost) * 100, 2)

    matrix.Clear()
    matrixScreen.Clear()
    pos_x=0
    pos_y=font.height
    line0 = graphics.DrawText(matrixScreen, font,1, pos_y,graphics.Color(255,255,255),"BTC: "+str(c>
    line1 = graphics.DrawText(matrixScreen, font,1, 18,graphics.Color(255,255,255),"HLD: "+coins+bt>
    if roi <= 0:
        line2 = graphics.DrawText(matrixScreen, font,1, 28,graphics.Color(255,0,0),"VAL: "+str(port>
        line3 = graphics.DrawText(matrixScreen, font,1, 38,graphics.Color(255,0,0),"YLD: "+str(gain>
        line4 = graphics.DrawText(matrixScreen, font,1, 48,graphics.Color(255,0,0),"ROI: "+str(roi)>
    else:
        line2 = graphics.DrawText(matrixScreen, font,1, 28,graphics.Color(0,255,0),"VAL: "+str(port>
        line3 = graphics.DrawText(matrixScreen, font,1, 38,graphics.Color(0,255,0),"YLD: "+str(gain>
        line4 = graphics.DrawText(matrixScreen, font,1, 48,graphics.Color(0,255,0),"ROI: "+str(roi)>
    line5 = graphics.DrawText(matrixScreen, font,1, 58,graphics.Color(255,255,255),"DCA: "+str(roun>
    matrixScreen = matrix.SwapOnVSync(matrixScreen)
    time.sleep(20)
