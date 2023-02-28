# This code is primarily support functions intended to help the user and to assist other functions

import yfinance as yf
from datetime import timedelta


# set the date ranges to focus on 5 weekdays, based on a given input
# the test data will be from the input date forward, historical data will be from the input date backwards
# provide:
#   start_date  :   date to use as a starting point
# returns: list
#   end_date    :   fifth business day forward from start point (to use for testing)
#   hist_start  :   fifth business day back from start point (to pull historical data from)
#   hist_end    :   one business day back from start point (to pull historical data to)
def date_ranges(start_date):
    if start_date.weekday() == 0:
        end_date = start_date + timedelta(days=5)
        hist_end = start_date - timedelta(days=2)
        hist_start = start_date - timedelta(days=8)
    elif start_date.weekday() == 5:
        end_date = start_date + timedelta(days=7)
        hist_end = start_date
        hist_start = start_date - timedelta(days=5)
    elif start_date.weekday() == 6:
        end_date = start_date + timedelta(days=6)
        hist_end = start_date - timedelta(days=1)
        hist_start = start_date - timedelta(days=7)
    else:
        end_date = start_date + timedelta(days=7)
        hist_end = start_date
        hist_start = start_date - timedelta(days=7)
    return [end_date, hist_start, hist_end]


# kicks out target date ranges for a single days worth of historical data (no forward-looking test data)
# provide: start_date - date to use as a starting point
# returns: hist_start - one business day back from the starting point to use for historical data pull
def single_date(start_date):
    if start_date.weekday() == 0:
        hist_start = start_date - timedelta(days=3)
    elif start_date.weekday() == 6:
        hist_start = start_date - timedelta(days=2)
    else:
        hist_start = start_date - timedelta(days=1)
    return hist_start


# prepare historical data from stock listing using data from yahoo
# pull the target stock's data over five minute intervals for a given date range
# add a column for 'average' of that 5 minute interval based on the open and close price and remove extra columns
# provide:
#   target_stock    :   stock ticker (ex. 'MSFT'),
#   start_date      :   date to start data pull
#   end_date        :   date to end data pull
# return:
#   prepped_data    :   pulled from yahoo finance at 5 minute intervals for a date range, with prices averaged out
def prep_data(target_stock, start_date, end_date):
    prepped_data = yf.Ticker(target_stock).history(interval='5m', start=start_date, end=end_date)
    prepped_data = prepped_data[['Open', 'Close']]
    prepped_data['Average'] = (prepped_data['Open'] + prepped_data['Close']) / 2
    return prepped_data


# recommend target sell/buy prices for a stock based on standard deviation from average over a given date range
# you can use a factor for std deviation other than 1 (ex target .8 of a std deviation instead of 1)
# provide:
#   target_stock    :   stock ticker (ex. 'MSFT')
#   start_date      :   date to start data pull
#   std_use         :   factor of standard deviation to use to determine prices based on std dev from average
#   day_count       :   how many days we will pull historical data for (either 1 or 5)
# returns: list
#   buy_price       :   recommended purchase price based on provided inputs
#   sell_price      :   recommended sell price based on provided inputs
def recommend_points(target_stock, start_date, std_use, day_count):
    if day_count == 5:
        date_list = date_ranges(start_date)
        hist_start = date_list[1]
        hist_end = date_list[2]
    elif day_count == 1:
        hist_start = single_date(start_date)
        hist_end = start_date
    else:
        exit('Recommend_points method will only work to pull data from 1 or 5 days back.  Update day_count value.')

    # pull historical data for date range at 5 minute increments, determine recommended sell/buy price
    historical_data = prep_data(target_stock, hist_start, hist_end)
    baseline_price = historical_data['Average'].mean()
    standard_deviation = historical_data['Average'].std() * std_use
    buy_price = baseline_price - standard_deviation
    sell_price = baseline_price + standard_deviation
    buy_price = round(buy_price, 2)
    sell_price = round(sell_price, 2)
    return [buy_price, sell_price]
