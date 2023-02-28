# This primarily contains functions used for testing a particular stock to see how compatible it is with this logic

from datetime import timedelta, date
import numpy as np
from support_function import prep_data, recommend_points
from robin_stocks.robinhood import get_instruments_by_symbols, get_name_by_symbol


# TEST FUNCTIONS to help determine if a stock might be a good option
# ==============================================================================================================
# look at a particular stock and report what would have been bought and sold over a one-day period
# with a given start date, the following five days will be the 'test' range you would buy/sell over
# you can also provide a target price to sell at or buy at, as well as how much to spend on each purchase
# if price drops below the target buy price, a buy would be triggered the moment price starts to rise again
# once a buy is triggered, it will start looking to sell (it will not buy multiple times in a row)
# the sell will trigger if price goes above your target sell price the moment price starts to fall again
# it'll use 5m intervals and that will only work for the last 60ish days, so it's not exact but is a good reference
# returns amount bought, sold, count (count of full cycle transactions bought/sold), profit, holding (stock remaining)
# provide:
#   target_stock    :   stock ticker (ex. 'MSFT')
#   start_date      :   initial date to use as a starting point for pulling data
#   buy_price       :   target price to buy stock at
#   sell_price      :   target price to sell stock at
#   spend           :   dollar amount you want to spend for each purchase (minimum of $1 for fractional trades)
# returns: [bought, sold, count, profit, holding]
#   bought          :   amount of stock bought (in dollars)
#   sold            :   amount of stock sold (in dollars)
#   count           :   number of full transactions (bought and sold pairings) completed
#   profit          :   dollar amount of profit off full transactions (ignores remaining stock)
#   holding         :   amount of stock that went unsold
def analyze_stock(target_stock, start_date, buy_price, sell_price, spend):
    end_date = start_date + timedelta(days=1)

    # break out the data set into factors to help determine when to buy and when to sell
    test_data = prep_data(target_stock, start_date, end_date)
    test_data['Buy'] = np.where(test_data['Average'] <= buy_price, 'buy', '')
    test_data['Sell'] = np.where(test_data['Average'] >= sell_price, 'sell', '')
    test_data['shifted'] = test_data['Average'].shift(1)
    test_data['Rise'] = np.where(test_data['shifted'] < test_data['Average'], 'rise', '')
    test_data['Drop'] = np.where(test_data['shifted'] > test_data['Average'], 'drop', '')
    test_data['Actual Buy'] = np.where((test_data['Rise'] == 'rise') & (test_data['Buy'] == 'buy'),
                                       test_data['Average'], '0')
    test_data['Actual Sell'] = np.where((test_data['Drop'] == 'drop') & (test_data['Sell'] == 'sell'),
                                        test_data['Average'], '0')

    # create a record of actual purchase/sell points
    flag = 'buy'
    flag_column = 'Actual Buy'
    record = list()
    for index, row in test_data.iterrows():
        if float(row[flag_column]) > 0:
            record.append([row[flag_column], flag])
            if flag == 'buy':
                flag = 'sell'
                flag_column = 'Actual Sell'
            else:
                flag = 'buy'
                flag_column = 'Actual Buy'

    # if we bought something, check the end of day close price to see if we should sell it
    if len(record) != 0:
        if flag == 'sell':
            bought_at = float(record[int(len(record) - 1)][0])
            close_price = float(test_data['Average'].iat[-1])
            if bought_at < close_price:
                record.append([close_price, 'sell'])

    # if record is empty, no buys made so no buy/sell data to report
    # otherwise, figure out buy/sell/profit data
    if len(record) == 0:
        bought = 0
        sold = 0
        count = 0
        profit = 0
        holding = 0
    else:
        bought = 0
        sold = 0
        count = 0
        percent_holding = 0
        for item in range(len(record)):
            if record[item][1] == 'buy':
                bought = bought + spend
                percent_holding = spend / float(record[item][0])
            elif record[item][1] == 'sell':
                sold = sold + (percent_holding * float(record[item][0]))
                count = count + 1

        profit = sold - bought
        if (count * spend) < bought:
            holding = percent_holding
            profit = profit + spend
        else:
            holding = 0

    return [bought, sold, count, profit, holding]


# for a given stock, pull its recommend prices and use those to analyze the stock using analyze_stock
# provide:
#   start_date      :   initial date to use for date ranges
#   target_stock    :   stock ticker (ex. 'MSFT')
#   std_use         :   factor of standard deviation to use to determine how far away from average to set prices
#   max_spend       :   dollar amount (minimum $1 for fractional trades) to be spent on each purchase
# returns info from analyze_stock function
def full_check(start_date, target_stock, std_use, max_spend):
    prices = recommend_points(target_stock, start_date, std_use, 5)
    info = analyze_stock(target_stock, start_date, prices[0], prices[1], max_spend)
    return info


# analyze a stock using full_check for the last 'x' days
# this will run a series of checks on the target stock for the past 'x' days to get a range of reference data
# provide:
#   target_stock    :   stock ticker (ex. 'MSFT')
#   std_use         :   factor of standard deviation to use to determine how far away from average to set prices
#   max_spend       :   dollar amount (minimum $1 for fractional trades) to be spent on each purchase
#   day_count       :   how many days back do you want to pull data for (max of 60)
# returns a message with the test data to be displayed on the QT GUI form
def test_x_days(target_stock, std_use, max_spend, day_count):
    start_date = date.today()
    bought = 0
    sold = 0
    profit = 0
    count = 0
    holding = 0
    for n in list(range(0, day_count)):
        start_date = start_date - timedelta(days=1)
        if not start_date.weekday() == 5 and not start_date.weekday() == 6:
            info = full_check(start_date, target_stock, std_use, max_spend)
            bought = bought + info[0]
            sold = sold + info[1]
            count = count + info[2]
            profit = profit + info[3]
            holding = holding + info[4]
    msg = f'''Analysis of {target_stock} over the last {day_count} days:
Bought ${round(bought,5)} in total, sold ${round(sold, 5)} in total, for {count} complete buy/sell transactions.
Total profit was ${round(profit, 5)} with {round(holding, 5)} shares still in holding'''
    return msg


# checks a stock to make sure it can sell in fractional amounts, is active, and is tradeable
# build a message to display on the QT GUI form based on stock info, returns that message
# TODO - return a list with message and whether or not to proceed?
def check_stock(target_stock):
    if len(get_name_by_symbol(target_stock)) > 0:
        sum_info = get_instruments_by_symbols(target_stock)
        sum_dict = sum_info[0]
        state = sum_dict['state']
        tradeable = sum_dict['tradeable']
        fractional = sum_dict['fractional_tradability']
        if state == 'active' and tradeable == True and fractional == 'tradable':
            msg = 'This stock is active and allows fractional trades.'
        else:
            msg = 'WARNING: Unfortunately, this stock is not compatible with this code.'
            if not state == 'active':
                msg = msg + '\n' + 'ERROR: This stock is not currently active.'
            if not tradeable == True:
                msg = msg + '\n' + 'ERROR: This stock is not currently tradeable.'
            if not fractional == 'tradable':
                msg = msg + '\n' + 'ERROR: This stock does not allow fractional trades.'
            msg = msg + '\n' + '\n' + 'Please select a new stock and try again.'
    else:
        msg = 'WARNING: There was an error finding this stock, please check for typos or try a new stock.'
    return msg
