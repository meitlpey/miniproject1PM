# INF601 - Advanced Programming in Python
# Peyton Meitler
# Mini Project 1

import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
from pathlib import Path


def getClosing(ticker):
    #gets the closing prices
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d") # get historical market data

    closingList = []

    for price in hist['Close']:
        closingList.append(price)

    return  closingList

def printGraphs(stock):
    #Prints Graphs
    stockClosing = np.array(getClosing(stock))

    len(stockClosing)

    days = list(range (1,len(stockClosing)+1))
    #for plotting graph
    plt.plot(days, stockClosing)

    #This gets the min and max for the graph
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]

    #form [xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_price-1, high_price+1])

    #sets the X and Y labels
    plt.ylabel("Closing Price")
    plt.xlabel("Days")
    #Puts a title on the graph
    plt.title("Closing Price for " + stock)
    #Saves the plot
    savefile = "charts/" + stock + ".png"
    plt.savefig(savefile)
    #shows the graph
    plt.show()

def getStocks():

    stocks = []
    #getting the users stocks
    print("Please enter five stocks to graph:")
    for i in range(1,6):
        while True:
            print("Enter stock ticker number " + str(i))
            ticker = input("> ")
            #checking the stocks
            try:
                print("Checking Ticker")
                stock = yf.Ticker(ticker)
                stock.info
                stocks.append(ticker)
                print("Valid ticker.")
                break
            except:
                print("That is not a valid stock. Please enter another.")
                continue
    return stocks

#Start of the program
#Creates our charts folder
try:
    # Create charts File
    Path("charts").mkdir()
except FileExistsError:
    pass

for stock in getStocks():
    getClosing(stock)
    printGraphs(stock)