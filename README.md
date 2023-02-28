# Summary
Adds a basic user interface for previously developed Robinhood trading bot code.  Reference RobinhoodTradingBot repository to see where this originally came from (note that the trading bot has since been updated to include alternate approaches, which are not accounted for in this GUI).  This is an example trading bot built using the (unofficial) Robinhood API. It uses a cash account from Robinhood to get around day trading limits, and will target a provided stock at pre-determined purchase and sell prices. This is NOT intended to be stock advice in any way, and was just a hobby project for fun. The code will also recommend buy/sell prices to you based on historical price data, and you can 'test' stocks to see how well they would have performed over the last 30 days using this code's logic. The recommended buy/sell prices are determined using standard deviation from average of historical price data. The primary code will purchase stock in pre-determined dollar amounts when the price falls below the target purchase price and sell when price rises above target sell price. 

Primary Logic - for a selected stock, this code seeks to buy and sell at certain prices. If the price drops below your target purchase price, the code will check if the price is falling or rising. At the first sign of a rising price, the code will execute a purchase to try to buy at the lowest point. After buying, the code will attempt to sell that stock by waiting for the price to climb above your target sell price and waiting for the first sign of the price falling again (trying to buy at the high point). This process will repeat all day, buying and selling the target stock with the specified target prices and spend amount, and the system will generate a summary report at the end of the day with what it accomplished.

# What are the files in this project?
qt_gui.py - this is the primary file containing the user interface and controlling the performance of the interface, including button connections.

robinhood_function.py - this contains login functions for Robinhood as well as the code to actually execute buying and selling of a target stock throughout the day.

testing_function.py - this contains code for users test a particular stock to see how compatible it is with the logic used in this code. They can test with custom buy/sell prices or recommended buy/sell prices, and can test over a variety of date ranges for historical data to see how the code would have performed. The alternate buy/sell approach can also be tested using functions in this file.

support_function.py - contains functions used to help determine recommended purchase and sell prices (includes functions that determine date ranges focused on business days and functions that pull and prep data pulled for a specific stock over a specified date range). Recommended prices are based on a provided factor of standard deviation away from the average based on historical price data.


# What libraries are used? 
robin_stocks.robinhood - https://robin-stocks.readthedocs.io/en/latest/robinhood.html - used for robinhood API (unofficial)

time - https://docs.python.org/3/library/time.html - sleep method used to add delays to loops to allow time for stock prices to change

datetime - https://docs.python.org/3/library/datetime.html - used to create date ranges from a given start date

yfinance - https://pypi.org/project/yfinance/ - uses yahoo api's to pull historical price data for stocks (note: personal use only)

numpy - https://numpy.org/ - used to prepare and analyze historical price data

PyQt6 - link - used QT Creator/Designer to build an initial user interface, converted to .py file using pyuic6 and used pyqt6 library in python to make final adjustments and develop buttons

sys, os, getpass, pickle, random - all provide general support to adjusting some of the API code to cooperate more easily with the user interface and to launch the user interface successfully. 
