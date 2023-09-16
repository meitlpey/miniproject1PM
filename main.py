# INF601 - Advanced Programming in Python
# Peyton Meitler
# Mini Project 1

#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.


import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np


def getClosing(ticker):
    #gets the closing prices
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d") # get historical market data

    closingList = []

    for price in hist['Close']:
        closingList.append(price)

    return  closingList
#these are thee five stocks you want to track
stocks =["MSFT", "AAPL", "GME", "SONY", "META"]

for stock in stocks:

    stockClosing = np.array(getClosing(stock))

    len(stockClosing)

    days = list(range (1,len(stockClosing)+1))
    #for plotting graph
    plt.plot(days, stockClosing)

    #This gets the min and max for the graph
    prices = getClosing(stock)
    prices.sort()
    low_prices = prices[0]
    high_price = prices[-1]

    #form [xmin, xmax, ymin, ymax]
    plt.axis([1, 10, low_prices-1,high_price+1])

    #sets the X and Y labels
    plt.ylabel("Closing Price")
    plt.xlabel("Days")
    #Puts a title on the graph
    plt.title("Closing Price for " + stock)
    #shows the graph
    plt.show()


