import requests
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
import sys
import time


# Get the bitcoin price right now
def bitcoin_price():
    url = 'https://www.bitstamp.net/api/ticker/'
    response = requests.get(url)
    data = response.json()
    price = data['last']

    response =  "The current price of bitcoin is: $ " + str(price)
    return response

def eth_price():
    url = 'https://api.coingecko.com/api/v3/coins/ethereum'
    response = requests.get(url)
    data = response.json()
    price = data['market_data']['current_price']['usd']

    response =  "The current price of ethereum is: $ " + str(price)
    return response

def bnb_price():
    url = 'https://api.binance.com/api/v3/ticker/price?symbol=BNBETH'
    response = requests.get(url)
    data = response.json()
    price = data['price']

    response =  "The current price of BNB is: $ " + str(price)
    return response

def crypto_price():
    response = bitcoin_price() + "\n" + eth_price() + "\n" + bnb_price()

   # print("Crypto Response send!")
    return response

