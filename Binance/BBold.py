import sys
# append current python modules' folder path
# example: need to import module.py present in '/path/to/python/module/not/in/syspath'
sys.path.append('C:\\Users\\bryan\\Documents')
from APIcode import api_key
from APIcode import api_secret
import telegramtest


print(api_secret)

import os
if os.name == 'nt':
    import sys
    # append current python modules' folder path
    # example: need to import module.py present in '/path/to/python/module/not/in/syspath'
    sys.path.append('C:\\Users\\bryan\\Documents')
    from APIcode import api_key
    from APIcode import api_secret



api_key = ''
api_secret = ''

from binance.client import Client
import requests
import time as tm
import datetime
client = Client(api_key, api_secret)
from decimal import Decimal
import numpy as np
import talib


def lastpricefunc(symbol):
    marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
    res = requests.get(marketprices)
    data = res.json()
    volume = float(data['quoteVolume'])
    priceNow = float(data['lastPrice'])
    return priceNow, volume

def klinesinfo(symbol, start_str, time, lendele):
    klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
    high = [float(entry[2]) for entry in klines]
    low = [float(entry[3]) for entry in klines]
    close = [float(entry[4]) for entry in klines]
    volume = [float(entry[5]) for entry in klines]
    high = np.asarray(high)
    low = np.asarray(low)
    close = np.asarray(close)
    volume = np.asarray(volume)
    if lendele == True:
        high = np.delete(high, len(high)-1,0)
        low = np.delete(low, len(low)-1,0)
        close = np.delete(close, len(close)-1,0)
        volume = np.delete(volume, len(volume)-1,0)
    return high, low, close, volume

def positiefbm():
    klines = client.get_historical_klines(symbol='BTCEUR', start_str='240 minutes ago UTC', interval='1m')
    opent = [float(entry[1]) for entry in klines]
    opent = np.asarray(opent)
    priceNow, volume = lastpricefunc('BTCEUR')
    if priceNow > opent[1]:
        klines = client.get_historical_klines(symbol='BTCEUR', start_str='60 minutes ago UTC', interval='1m')
        opent = [float(entry[1]) for entry in klines]
        opent = np.asarray(opent)
        priceNow, volume = lastpricefunc('BTCEUR')
        if priceNow > opent[1] * 1.001:
            return True
    return False

while True:
    test = positiefbm()
    print(test)

# start_str = '100 minutes ago UTC'

# klines = client.get_historical_klines(symbol='BTCEUR', start_str=start_str , interval='1m')
# opent = [float(entry[1]) for entry in klines]
# high = [float(entry[2]) for entry in klines]
# low = [float(entry[3]) for entry in klines]
# close = [float(entry[4]) for entry in klines]
# volume = [float(entry[5]) for entry in klines]
# high = np.asarray(high)
# low = np.asarray(low)
# close = np.asarray(close)
# volume = np.asarray(volume)
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['quoteVolume'])
# priceNow = float(data['lastPrice'])
# print(opent[-1])
# print(priceNow)


# order= client.order_oco_sell(
#     symbol= 'BTCEUR',                                            
#     quantity= 0.000921,                                            
#     price= '52000', #BOVENSTE PRIJS                                           
#     stopPrice= '44100', #STOP                                           
#     stopLimitPrice= '44000', #DOOR ONDER
#     stopLimitTimeInForce=client.TIME_IN_FORCE_GTC)


# order= client.order_oco_sell(
#     symbol= 'BTCUSDT',                                            
#     quantity= 1.00000,                                            
#     price= '32000.07',                                            
#     stopPrice= '29283.03',                                            
#     stopLimitPrice= '29000.00',                                            
#     stopLimitTimeInForce= 'FOK')

# info = client.get_symbol_info(symbol)
# minprijs = float(info['filters'][0]['minPrice'])
# output = f"{minprijs:.9f}"
# # minimum = 0.001
# symbolbalace = client.get_asset_balance(asset='TRB')
# print(symbolbalace)
# symbolbalace = float(symbolbalace['locked'])
# symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
# print(symbolbalace)


# a = Decimal('1460356156116843.000000')
# b = Decimal('2301.93138123')


# symbol = "FILBTC"

# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# orderprijs = 0.0029136
# breakeven = orderprijs * 1.00075
# eersteinleg = btc_balance / 4
# hoeveelheid = eersteinleg / orderprijs
# info = client.get_symbol_info(symbol)
# minimum = float(info['filters'][2]['minQty'])
# hoeveelheid = float(round(hoeveelheid, len(str(minimum)) -2))
# a = Decimal(str(hoeveelheid))
# b = Decimal('0.01')
# c = float(Decimal(str(hoeveelheid)) - Decimal('0.01'))
# print(type(c))
# print(c)

# #LENGTE BEREKENEN VAN MINIMUM
# if len(str(minimum)) > 3:
#     hoeveelheid = float(Decimal(str(hoeveelheid)) - Decimal('0.01'))
# elif  len(str(minimum)) == 3:
#     hoeveelheid = float(Decimal(str(hoeveelheid)) - Decimal('0.1'))
# print(minimum)
# print(hoeveelheid)
# print(orderprijs)



# symbol = 'QTUMBTC'
# order = client.order_limit_buy(symbol=symbol,quantity=0.41,price='0.0002619')
# clientOrderId = order['orderId']
# tm.sleep(1)
# orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
# hoeveelheidintrade = float(orderstatus['executedQty'])
# print(hoeveelheidintrade)

# info = client.get_symbol_info('BTCEUR')
# print(info)
# minimum = float(info['filters'][2]['minQty'])
# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# btc_balance = round(btc_balance,5)
# print(btc_balance)
# order= client.order_oco_sell(
#     symbol= 'BTCEUR',                                            
#     quantity= btc_balance,                                            
#     price= '52000.00', #BOVENSTE PRIJS                                           
#     stopPrice= '44100.00', #STOP                                           
#     stopLimitPrice= '44000.00', #DOOR ONDER
#     stopLimitTimeInForce=client.TIME_IN_FORCE_GTC)
  
# tm.sleep(2)
# first = order['orders'][0]['orderId']
# firsttype = order['orderReports'][0]['type']
# second = order['orders'][1]['orderId']
# secondtype = order['orderReports'][1]['type']
# print(firsttype)
# print(secondtype)
# orderstatus = client.get_order(symbol="BTCEUR",orderId=first)
# orderstatus = orderstatus['status']
# print(orderstatus)
# result = client.cancel_order(
#     symbol='BTCEUR',
#     orderId=first)

# info = client.get_symbol_info('BNBBTC')
# print(info)

# minimum = info['filters'][2]['minQty']
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'BTCEUR'
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['volume'])
# priceNow = float(data['lastPrice'])
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'BNBBTC'
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['volume'])
# priceNow2 = float(data['lastPrice'])
# minimalebtcprijs = float(priceNow2) * float(minimum)
# euro = float(minimalebtcprijs) * float(priceNow)
# inleg = 8 / euro * float(minimum)
# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# btc_balance = btc_balance * float(priceNow)
# print(inleg)
# inleg = round(inleg, 2)
# print(btc_balance)
# print(minimum)
# print(minimalebtcprijs)
# print(euro)
# order = client.order_limit_buy(symbol='BNBBTC',quantity=inleg,price=0.0061665)
# print(order)

# symbol = "XVSBTC"
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['volume'])
# priceNow = float(data['lastPrice'])
# orderprijs = priceNow

# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# eersteinleg = btc_balance / 4
# hoeveelheid = eersteinleg / orderprijs
# info = client.get_symbol_info(symbol)
# minimum = float(info['filters'][2]['minQty'])
# hoeveelheid = float(round(hoeveelheid, len(str(minimum)) -2))
# print(hoeveelheid)





# orderprijs = 0.035142

# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# orderprijs = orderprijs
# breakeven = orderprijs * 1.00075
# print(btc_balance / 4)
# eersteinleg = btc_balance / 4
# hoeveelheid = eersteinleg / orderprijs
# test = 0.00007644 / 0.035142
# print(hoeveelheid)
# hoeveelheid = float(round(hoeveelheid, 2) - 0.01)
# print(hoeveelheid)
# print(orderprijs)

# time_res = client.get_server_time()
# info = client.get_account()
# balance = client.get_asset_balance(asset='test')
# status = client.get_account_status()
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'BNBBTC'
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['volume'])
# priceNow = float(data['lastPrice'])
# btc_balance = client.get_asset_balance(asset='BTC')
# btc_balance = float(btc_balance['free'])
# marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'QTUMBTC'
# res = requests.get(marketprices)
# data = res.json()
# volume = float(data['volume'])
# priceNow = float(data['lastPrice'])
# hoeveelheid = btc_balance / 4
# hoeveelheid = hoeveelheid / priceNow
# print(hoeveelheid)
# hoeveelheid = float(round(hoeveelheid, 2) - 0.01)
# print(hoeveelheid)
# info = client.get_symbol_info('BNBBTC')
# print(info)

# print(info['filters'][2]['minQty'])
# print(info)
# 0.25 hvl
# 0.0002918 price




# order = client.order_limit_sell(symbol='BTCEUR',quantity=0.000305,price=50000)
# print(order)
# clientOrderId = order['orderId']
# time.sleep(1)
# orderstatus = client.get_order(symbol='BTCEUR',orderId=clientOrderId)
# orderstatus = orderstatus['status']
# while True:
#   klines = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1MINUTE, "11:52 am ,7 April, 2021", "0:52 pm, 7 April, 2021")
#   klines = client.get_historical_klines("BTCEUR", Client.KLINE_INTERVAL_1MINUTE, "")
#   print(klines)


#   klines = client.get_historical_klines(symbol='BTCEUR', start_str='60 minutes ago UTC' , interval='3m')
#   opent = [float(entry[1]) for entry in klines]
#   marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'BTCEUR'
#   res = requests.get(marketprices)
#   data = res.json()
#   priceNow = float(data['lastPrice'])
#   persentage = opent[-1] / priceNow * 100
#   nutijd = datetime.datetime.now()
#   print("interval 3m", persentage, nutijd)
#   klines = client.get_historical_klines(symbol='BTCEUR', start_str='60 minutes ago UTC' , interval='1h')
#   opent = [float(entry[1]) for entry in klines]
#   marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + 'BTCEUR'
#   res = requests.get(marketprices)
#   data = res.json()
#   priceNow = float(data['lastPrice'])
#   opent = opent[0] - priceNow
#   persentage = opent / priceNow * 100
#   nutijd = datetime.datetime.now()
#   print("interval 1h", persentage, nutijd)
