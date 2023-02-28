# This file is the primary use file for this project
# Provide your login info and stock info before running the code
# Note that stock will be bought, then sold.  The code will not buy multiple times in a row.
# Stock remaining at the end of the day (unsold) will be left for the user to decide what to do with it.
# TODO - check to sell stock held at the end of the day

import robin_stocks.robinhood as rs
import getpass
import os
import pickle
import random
from robin_stocks.robinhood.helper import *
from robin_stocks.robinhood.urls import *
from time import sleep
from datetime import datetime


# SOURCE ADJUSTMENTS
# =================================================================================================================
# The following class and several functions are being used to adjust some of the source code
# This changes how the log in behavior works to cooperate more smoothly with the GUI
class MFAException(Exception):
    """Raised when an MFA is required but not provided"""
    pass


# from source code
def generate_device_token():
    rands = []
    for i in range(0, 16):
        r = random.random()
        rand = 4294967296.0 * r
        rands.append((int(rand) >> ((3 & i) << 3)) & 255)

    hexa = []
    for i in range(0, 256):
        hexa.append(str(hex(i + 256)).lstrip("0x").rstrip("L")[1:])

    id = ""
    for i in range(0, 16):
        id += hexa[rands[i]]

        if (i == 3) or (i == 5) or (i == 7) or (i == 9):
            id += "-"

    return (id)


# from source code
def respond_to_challenge(challenge_id, sms_code):
    url = challenge_url(challenge_id)
    payload = {
        'response': sms_code
    }
    return (request_post(url, payload))


# from source code, adjusted
# This function logs in using the same logic as the API but ignores any instance of MFA to avoid messages.
def login_no_mfa(username=None, password=None, expiresIn=86400, scope='internal', by_sms=True, store_session=True,
                 mfa_code=None, pickle_name=""):
    device_token = generate_device_token()
    home_dir = os.path.expanduser("~")
    data_dir = os.path.join(home_dir, ".tokens")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    creds_file = "robinhood" + pickle_name + ".pickle"
    pickle_path = os.path.join(data_dir, creds_file)
    # Challenge type is used if not logging in with two-factor authentication.
    if by_sms:
        challenge_type = "sms"
    else:
        challenge_type = "email"

    url = login_url()
    payload = {
        'client_id': 'c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS',
        'expires_in': expiresIn,
        'grant_type': 'password',
        'password': password,
        'scope': scope,
        'username': username,
        'challenge_type': challenge_type,
        'device_token': device_token
    }

    if mfa_code:
        payload['mfa_code'] = mfa_code

    # If authentication has been stored in pickle file then load it. Stops login server from being pinged so much.
    if os.path.isfile(pickle_path):
        # If store_session has been set to false then delete the pickle file, otherwise try to load it.
        # Loading pickle file will fail if the acess_token has expired.
        if store_session:
            try:
                with open(pickle_path, 'rb') as f:
                    pickle_data = pickle.load(f)
                    access_token = pickle_data['access_token']
                    token_type = pickle_data['token_type']
                    refresh_token = pickle_data['refresh_token']
                    # Set device_token to be the original device token when first logged in.
                    pickle_device_token = pickle_data['device_token']
                    payload['device_token'] = pickle_device_token
                    # Set login status to True in order to try and get account info.
                    set_login_state(True)
                    update_session(
                        'Authorization', '{0} {1}'.format(token_type, access_token))
                    # Try to load account profile to check that authorization token is still valid.
                    res = request_get(
                        positions_url(), 'pagination', {'nonzero': 'true'}, jsonify_data=False)
                    # Raises exception is response code is not 200.
                    res.raise_for_status()
                    return({'access_token': access_token, 'token_type': token_type,
                            'expires_in': expiresIn, 'scope': scope, 'detail': 'logged in using authentication in {0}'.format(creds_file),
                            'backup_code': None, 'refresh_token': refresh_token})
            except:
                print(
                    "ERROR: There was an issue loading pickle file. Authentication may be expired - logging in normally.", file=get_output())
                set_login_state(False)
                update_session('Authorization', None)
        else:
            os.remove(pickle_path)

    # Try to log in normally.
    if not username:
        username = input("Robinhood username: ")
        payload['username'] = username

    if not password:
        password = getpass.getpass("Robinhood password: ")
        payload['password'] = password

    data = request_post(url, payload)
    # Handle case where mfa or challenge is required.
    if data:
        if 'mfa_required' in data:
            raise MFAException('mfa required')
        else:
            raise Exception(data['detail'])
    else:
        raise Exception('Error: Trouble connecting to robinhood API. Check internet connection.')


# USER LOGIN
# =================================================================================================================
# This following two functions log the user in and return a message once they are logged in successfully.
# TODO - could combine these two functions into one based on whether or not an MFA is provided
# If the user does not provide an MFA token, it is assumed to be None.  If one is needed, the user will provide it
# in the mfa box on the form and log in again.
# If there is an error logging in, an error message will show.  The user will only be logged in for 10 hours.
def robinhood_login(username, password, mfa=None):
    try:
        if login_no_mfa(username, password, 36000):
            msg = 'You are successfully logged in!  You can now move to step two and enter stock information.'
    except MFAException:
        msg = "Your account requires multi-factor authentication.  This code is usually sent via email or text.  " \
              "Enter the code into the MFA box and click the Send MFA button to proceed. "
    except Exception:
        msg = "There was an error logging in to your account - check your username and password to make sure they are " \
              "correct. "
    return msg


# this code logs in with a provided MFA
# returns a message for display on the QT GUI form about log in being successful or not
def robinhood_login_mfa(username, password, mfa=None):
    try:
        if rs.login(username, password, 36000, mfa_code=mfa):
            msg = 'You are successfully logged in!  You can now move to step two and enter stock information.'
    except Exception:
        msg = "There was an error logging in to your account - check your username, password, and MFA to make sure " \
              "they are correct. "
    return msg


# PRIMARY CODE
# =================================================================================================================
# This function will buy or sell a target stock based on a predetermined target price range
# It will run from 9:05 am to 4:55 pm (this can be changed in the code)
# Check the price every minute to track if price is rising/falling and how it compares to the target buy/sell price
# It will first try to buy stock, then will attempt to sell that stock before buying anymore
# It will buy if the price is below the target buy price AND the price is no longer falling
# It will sell if the price is above the target sell price AND the price is no longer rising
# Stock held at the end of the day will be checked if it can be sold for ANY profit (no matter how small) or held
# provide:
#   target_stock    :   stock ticker (ex. 'MSFT')
#   spend           :   dollar amount to spend on each purchase (minimum $1 for fractional trades)
#   buy_price       :   target purchase price
#   sell_price      :   target sell price
# returns: summary message for display on QT GUI form regarding how much was sold/bought/profit/held
def purchase_by_price(target_stock, spend, buy_price, sell_price):

    # set default values, wait a minute to let prices shift a little so that we can figure if they are rising or falling
    action = 'buy'
    last_price = float(rs.stocks.get_latest_price(target_stock)[0])
    stock_amount = 0
    profit = 0
    bought = 0
    sold = 0
    transactions = 0
    sleep(60)

    # time range is set to 9:05am to 4:55pm, change it below if desired
    current_time = datetime.now()
    start_time = current_time.replace(hour=9, minute=5, second=0, microsecond=0)
    end_time = current_time.now().replace(hour=16, minute=55, second=0, microsecond=0)

    # while we are in the time range, execute code
    while start_time < current_time < end_time:

        # check to make sure we still have enough money left to keep buying stuff, otherwise kill it
        # if we are selling, then we aren't worried about this
        if action == 'buy':
            account_info = rs.profiles.load_account_profile()
            buying_power = float(account_info['buying_power'])
            if buying_power < spend:
                return 'Buying power is less than your specified spend amount.  The program will now stop running.'

        # pull current price of the target stock and compare to last known price to see if it's rising/falling
        current_price = float(rs.stocks.get_latest_price(target_stock)[0])
        if current_price < last_price:
            path = 'drop'
        elif current_price > last_price:
            path = 'rise'
        else:
            path = 'hold'
        last_price = current_price

        # trigger a buy if we are currently trying to buy, below our buy price, and price has turned to rise
        # flip the desired action to sell so the code will focus on opportunities to sell
        if action == 'buy' and path == 'rise' and current_price < buy_price:
            action = 'sell'
            last_price = float(rs.stocks.get_latest_price(target_stock)[0])
            stock_amount = round(spend / last_price, 6)
            # NOTE: source code order_buy_fractional_by_price fails after a recent Robinhood update
            #       instead, I'm using fractional buy by qty and calculating the corresponding qty
            print(rs.orders.order_buy_fractional_by_quantity(target_stock, stock_amount, timeInForce='gfd'))
            bought = bought + spend
            print(f'bought {stock_amount} at {current_time} at {current_price}')

        # trigger a sell if we are trying to sell, above our sell price, and price has turned to fall
        # flip action back to buy so the code will focus on purchase opportunities again
        if action == 'sell' and path == 'drop' and current_price > sell_price:
            action = 'buy'
            print(rs.orders.order_sell_fractional_by_quantity(target_stock, stock_amount, timeInForce='gfd'))
            transactions = transactions + 1
            sold = sold + (stock_amount * current_price)
            print(f'sold {stock_amount} at {current_time} at {current_price}')

        # wait one minute before checking again
        sleep(60)
        current_time = datetime.now()
    else:
        sum_msg = f'''Target Stock {target_stock} Daily Summary
==========================================
Total purchase amount: ${bought} 
Total sell amount: ${sold} 
Resultant profit: ${profit} with {stock_amount} stocks left over.'''
        return sum_msg
