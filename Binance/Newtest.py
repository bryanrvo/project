from binance.client import Client
import datetime as dt
import pandas as pd
import time
import numpy as np
import requests
import talib


client = Client('607f382f17ed1d00ed50eb440a8d9c56a5d40dd35b91d9865b8cf893dba2cd7c', ' ddc0cbea2cc02f7b5cccb3165851d65a20c7fd8f81a7aea3e7223a8809751e6b')
symbol = 'BTCEUR'
length = 20
width = 2
inposition = False
intervalunit = '1T'
start_str = '60 minutes ago UTC'
interval_data = '1m'
klines = client.get_historical_klines(symbol=symbol, start_str=start_str, interval=interval_data)
print(klines)
high = [float(entry[2]) for entry in klines]
low = [float(entry[3]) for entry in klines]
close = [float(entry[4]) for entry in klines]
opent = [float(entry[4]) for entry in klines]
verschil = opent[0] - opent[-1]
print(verschil)
# balance = client.get_asset_balance(asset='BTC')
# print(balance)

# D = pd.DataFrame(client.get_historical_klines(symbol=symbol, start_str=start_str , interval=interval_data))
# D.columns = ['open_time','open','high','low','close','volume','close_time','qav','num_trades','traker_base_vol','taker_quote_vol','is_best_match']
# D['open_date_time'] = [dt.datetime.fromtimestamp(x / 1000) for x in D.open_time.values]
# D['symbol'] = symbol
# D = D[['symbol','open','high','low','close','volume','num_trades','traker_base_vol','taker_quote_vol']]
   
# ticker = client.get_ticker()

# op = D['open']
# hi = D['high']
# lo = D['low']
# cl = D['close']
# vl = D['volume']

# balance = client.get_asset_balance(asset='BTC')
# inzetprijs = balance / 4 / float(close[-1])

import winsound
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second



# BB
test = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=interval_data)
close = [float(entry[4]) for entry in test]
close_array = np.asarray(close)
rsi = talib.RSI(close_array, timeperiod=14)
upper, middle, lower = talib.BBANDS(close_array, 20, 2, 2)
last_upper = upper[-1]
last_lower = lower[-1]
difuplow = last_upper - last_lower
persentage = difuplow / middle[-1] * 100

#STOCH
test = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=interval_data)
high = [float(entry[2]) for entry in test]
low = [float(entry[3]) for entry in test]
close = [float(entry[4]) for entry in test]
lastcloseprice = test[-1]
high = np.asarray(high)
low = np.asarray(low)
close = np.asarray(close)
slowk, slowd = talib.STOCH(high, low, close, fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BNBBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
times = ['1m', '3m', '5m']
# times = ['1m']

while True:
    for symbol in symbols:
        for time in times:
            marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
            res = requests.get(marketprices)
            data = res.json()
            volume = float(data['volume'])
            priceNow = float(data['lastPrice'])
            if priceNow > 0.0000250 and volume > 200:
                klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
                high = [float(entry[2]) for entry in klines]
                low = [float(entry[3]) for entry in klines]
                close = [float(entry[4]) for entry in klines]
                high = np.asarray(high)
                low = np.asarray(low)
                close = np.asarray(close)
                high = np.delete(high, len(high)-1,0)
                low = np.delete(low, len(low)-1,0)
                close = np.delete(close, len(close)-1,0)
                lastcloseprice = close[-1]
                slowk, slowd = talib.STOCH(high, low, close, fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
                upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                last_upper = upper[-1]
                last_lower = lower[-1]
                last_slowk = slowk[-1]
                last_slowd = slowd[-1]
                difuplow = last_upper - last_lower
                persentage = difuplow / middle[-1] * 100
                #STOCH
                if last_slowk < 20 and  last_slowd < 20:
                    #BB
                    if last_lower > lastcloseprice:
                        # if slowk[-2] < slowd[-2] and  slowk[-1] > slowd[-1] or slowd[-2] < slowk[-2] and  slowd[-1] > slowk[-1]:
                        if time == '1m' and persentage > 1 and persentage < 4:
                            #winsound.Beep(frequency, duration)
                            print("BUY BUY BUY", symbol, time)
                            #PRIJS WAARVOOR JE GEKOCHT HEB KOMT HIER TE STAAN
                            # res = requests.get(marketprices)
                            # data = res.json()
                            # orderprijs = float(data['lastPrice'])
                            # breakeven = float(data['lastPrice']) * 1.0075
                            orderprijs = float(close[-1])
                            breakeven = float(close[-1]) * 1.00075
                            print("Je hebt gekocht voor:", orderprijs)
                            print("Je breakevenlijn is:", breakeven)
                            inposition = True
                        elif time == '3m' or time == '5m' and persentage > 1 and persentage < 4:
                            #winsound.Beep(frequency, duration)
                            print("BUY BUY BUY", symbol, time)
                            #PRIJS WAARVOOR JE GEKOCHT HEB KOMT HIER TE STAAN
                            orderprijs = float(close[-1])
                            breakeven = float(close[-1]) * 1.00075
                            print("Je hebt gekocht voor:", orderprijs)
                            print("Je breakevenlijn is:", breakeven)
                            inposition = True
                        if inposition == True:
                            print("order placed")
                            while inposition == True:
                                res = requests.get(marketprices)
                                data = res.json()
                                priceNow = float(data['lastPrice'])
                                klines = client.get_historical_klines(symbol=symbol, start_str='10 minutes ago UTC' , interval=time)
                                close = [float(entry[4]) for entry in klines]
                                close = np.asarray(close)
                                close = np.delete(close, len(close)-1,0)
                                lastclosePrice = close[-1]
                                if orderprijs - ((middle[-1] - last_lower) * 1.01) > priceNow:
                                    print("NOG EEN ORDER PLAATSEN")
                                    inposition = False
                                elif lastclosePrice > breakeven * 1.002:
                                    print("WE ZITTEN IN DE WINST")
                                    while inposition == True:
                                        res = requests.get(marketprices)
                                        data = res.json()
                                        priceNow = float(data['lastPrice'])
                                        # print("TOP: ", middle[-1] * 0.992)
                                        # print("middle lijn", middle[-1])
                                        # print("DIT IS DE PRIJS DIE WE HEBBEN", priceNow)
                                        # print("breakeven: ", breakeven )
                                        if priceNow < breakeven * 1.002 and priceNow > breakeven * 1.0015:
                                            print("SELL SELL SELL EVERYTHING", symbol, time) # EVERYTHING
                                            winst = (priceNow - breakeven ) / priceNow
                                            print("je hebt verkocht voor:", priceNow, "dat is:", winst)
                                            inposition = False
                                        elif priceNow > middle[-1] * 0.992 and time == '1m':
                                            print("SELL SELL SELL EVERYTHING", symbol, time) #EVERYTHING
                                            winst = (priceNow - breakeven ) / priceNow
                                            print("je hebt verkocht voor:", priceNow, "dat is:", winst)
                                            inposition = False
                                        elif priceNow > middle[-1] * 0.992 and time != '1m':
                                            print("SELL SELL SELL 3 KWART", symbol, time) #3 KWART
                                            winst = (priceNow - breakeven ) / priceNow
                                            print("je hebt verkocht voor:", priceNow, "dat is:", winst)
                                            while inposition == True:
                                                klines = client.get_historical_klines(symbol=symbol, start_str='10 minutes ago UTC' , interval=time)
                                                close = [float(entry[4]) for entry in klines]
                                                close = np.asarray(close)
                                                close = np.delete(close, len(close)-1,0)
                                                upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                if close[-1] > middle[-1]:
                                                    inposition = False
                                                    #STOP LOSE ONDER BB MIDDELSTE LIJN
                                                    # while inposition == True:
                                                    #     klines = client.get_historical_klines(symbol=symbol, start_str='10 minutes ago UTC' , interval=time)
                                                    #     close = [float(entry[4]) for entry in klines]
                                                    #     close = np.asarray(close)
                                                    #     close = np.delete(close, len(close)-1,0)
                                                    #     upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                    #     if stoploseniet and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                    #         #STOPLOSE
                                                    #     inposition = False
                                                

                                             
                            
                    



#XLM TRX ICX EOS IOTA ONT QTUM ETC ADA XMR DASH NEO ATOM DOGE VET BAT OMG BTT

# for symbol in symbols:
#     price = 'https://api.binance.com/api/v1/ticker/price?symbol=' + symbol
#     res = requests.get(price)
#     res = res.json()
#     print(symbol)
#     lastprice = float(res['price'])

# marketprices = 'https://api.binance.com/api/v1/ticker/24hr?symbol=' + symbol
# res = requests.get(marketprices)
# data = res.sjon()
# lastprice = float(data['lastPrice'])
# print(lastprice)