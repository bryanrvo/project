from binance.client import Client
import datetime as dt
import pandas as pd
import time
import numpy as np
import requests
import talib


client = Client('', ' ')
symbol = 'WAVESBTC'
length = 20
width = 2

intervalunit = '1T'
start_str = '100 minutes ago UTC'
interval_data = '1m'


D = pd.DataFrame(client.get_historical_klines(symbol=symbol, start_str=start_str , interval=interval_data))
D.columns = ['open_time','open','high','low','close','volume','close_time','qav','num_trades','traker_base_vol','taker_quote_vol','is_best_match']
D['open_date_time'] = [dt.datetime.fromtimestamp(x / 1000) for x in D.open_time.values]
D['symbol'] = symbol
D = D[['symbol','open','high','low','close','volume','num_trades','traker_base_vol','taker_quote_vol']]
   
ticker = client.get_ticker()

op = D['open']
hi = D['high']
lo = D['low']
cl = D['close']
vl = D['volume']


test = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=interval_data)

close = [float(entry[4]) for entry in test]
close_array = np.asarray(close)

rsi = talib.RSI(close_array, timeperiod=14)
upper, middle, lower = talib.BBANDS(close_array, 20, 2, 2)
last_upper = upper[-1]
last_lower = lower[-1]
difuplow = last_upper - last_lower
persentage = difuplow / middle[-1] * 100
print(persentage)




# price = 'https://api.binance.com/api/v1/ticker/price?symbol=LTCBTC'
# res = requests.get(price)
# res = res.json()
# lastprice = float(res['price'])
# marketprices = 'https://api.binance.com/api/v1/ticker/24hr?symbol=' + symbol
# res = requests.get(marketprices)
# data = res.sjon()
# lastprice = float(data['lastPrice'])
# print(lastprice)