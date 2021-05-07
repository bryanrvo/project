api_key = ''
api_secret = ''

from binance.client import Client
import datetime as dt
import time as tm
import numpy as np
import requests
import talib
import datetime
import telegramtest
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import StochasticOscillator
from ta.trend import PSARIndicator

# text, chat = telegramtest.get_last_chat_id_and_text(telegramtest.get_updates())
# chat = 1702054190
# text = 'start'
# telegramtest.send_message(text, chat)


client = Client(api_key, api_secret)
symbolbalace = client.get_asset_balance(asset='BTC')
symbolbalace = float(symbolbalace['free'])
order= client.order_oco_sell(
    symbol= 'BTCEUR',                                            
    quantity= 0.0008,                                            
    price='52000.00', #BOVENSTE PRIJS                                           
    stopPrice= '40000.00', #STOP                                           
    stopLimitPrice= '39500.00', #DOOR ONDER
    stopLimitTimeInForce=client.TIME_IN_FORCE_GTC)
# inposition = False
# start_str = '100 minutes ago UTC'

# symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
# times = ['1m', '3m', '5m']

# nuopditmoment = client.get_asset_balance(asset='BTC')
# print(nuopditmoment)
# nuopditmoment = float(nuopditmoment['free'])
# text = "btc balance: " + str(nuopditmoment)
# telegramtest.send_message(text, chat)

# def lastpricefunc(symbol):
#     marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
#     res = requests.get(marketprices)
#     data = res.json()
#     volume = float(data['quoteVolume'])
#     priceNow = float(data['lastPrice'])
#     return priceNow, volume

# def klinesinfo(symbol, start_str, time, lendele):
#     klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
#     high = [float(entry[2]) for entry in klines]
#     low = [float(entry[3]) for entry in klines]
#     close = [float(entry[4]) for entry in klines]
#     volume = [float(entry[5]) for entry in klines]
#     high = np.asarray(high)
#     low = np.asarray(low)
#     close = np.asarray(close)
#     volume = np.asarray(volume)
#     if lendele == True:
#         high = np.delete(high, len(high)-1,0)
#         low = np.delete(low, len(low)-1,0)
#         close = np.delete(close, len(close)-1,0)
#         volume = np.delete(volume, len(volume)-1,0)
#     return high, low, close, volume

# from binance.exceptions import BinanceAPIException, BinanceWithdrawException


# def get_sma(prices, rate):
#     return prices.rolling(rate).mean()

# def get_bollinger_bands(prices, rate=20):
#     sma = get_sma(prices, rate)
#     std = prices.rolling(rate).std()
#     bollinger_up = sma + std * 2 # Calculate top band
#     bollinger_down = sma - std * 2 # Calculate bottom band
#     return bollinger_up, bollinger_down

# def binanceDataFrame(klines):
#     df = pd.DataFrame(klines,dtype=float, columns = ('Open Time',
#                                                                     'Open',
#                                                                     'High',
#                                                                     'Low',
#                                                                     'Close',
#                                                                     'Volume',
#                                                                     'Close time',
#                                                                     'Quote asset volume',
#                                                                     'Number of trades',
#                                                                     'Taker buy base asset volume',
#                                                                     'Taker buy quote asset volume',
#                                                                     'Ignore'))

#     df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
#     return df


# while True:
#     for symbol in symbols:
#         for time in times:
#             priceNow, volume = lastpricefunc(symbol)
#             if priceNow > 0.0000500 and volume > 150:
#                 high, low, close, volume = klinesinfo(symbol, start_str, time, True)
#                 volume = volume[-10:]
#                 lastcloseprice = close[-1]
#                 slowk, slowd = talib.STOCH(high, low, close, fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
#                 upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                
#                 klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
#                 df = binanceDataFrame(klines)
#                 df = df[:-1]
#                 indicator_bb = BollingerBands(df["Close"])
#                 df['bb_bbm'] = indicator_bb.bollinger_mavg()
#                 df['bb_bbh'] = indicator_bb.bollinger_hband()
#                 df['bb_bbl'] = indicator_bb.bollinger_lband()


                
#                 Stocha = StochasticOscillator(close=df["Close"],high=df["High"],low=df["Low"])
#                 slowk1 = Stocha.stoch_signal()
#                 slowd1 = slowk1.rolling(3).mean()
#                 slowk1 = np.asarray(slowk1)
#                 slowd1 = np.asarray(slowd1)
#                 print(symbol,time)
#                 print(slowk1[-1], slowk[-1])
#                 print(slowd1[-1], slowd[-1])

#                 #JUIST
#                 sarpoint1 = PSARIndicator(close=df["Close"],high=df["High"],low=df["Low"])
#                 psar = sarpoint1.psar()

#                 print(psar.iloc[-2],symbol,time)
  
                

                
#                 last_upper = upper[-1]
#                 last_lower = lower[-1]
#                 last_slowk = slowk[-1]
#                 last_slowd = slowd[-1]
#                 difuplow = last_upper - last_lower
#                 persentage = difuplow / priceNow * 100
                
#                 if last_slowk < 20 and  last_slowd < 20 and all(i >= 10 for i in volume):
#                     if last_lower > lastcloseprice:
#                         priceNow, volume = lastpricefunc(symbol)
                        
                    
                    


