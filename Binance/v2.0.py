from binance.client import Client
import os
import datetime as dt
import pandas as pd
import time
import numpy as np
import requests
import talib
import datetime
import winsound
frequency = 1500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
import telegramtest
import math

text, chat = telegramtest.get_last_chat_id_and_text(telegramtest.get_updates())
text = 'start'
telegramtest.send_message(text, chat)

day = datetime.datetime.today().weekday()
print(day)
nutijd = datetime.datetime.now()
start_time = nutijd.replace(hour=7, minute=0, second=0, microsecond=0)
end_time = nutijd.replace(hour=22, minute=0, second=0, microsecond=0) 

client = Client('', ' ')
inposition = False
start_str = '100 minutes ago UTC'

symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BNBBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
times = ['1m', '3m', '5m']

#account = client.get_asset_balance(asset='BTC')
btc_balance = 0.004
while True:
    if nutijd > start_time and nutijd < end_time and datetime.datetime.today().weekday() < 6:
        for symbol in symbols:
            for time in times:
                marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
                res = requests.get(marketprices)
                data = res.json()
                volume = float(data['volume'])
                priceNow = float(data['lastPrice'])
                priceChangePercent = float(data['priceChangePercent'])
                if priceNow > 0.000250 and volume > 200:
                    klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
                    high = [float(entry[2]) for entry in klines]
                    low = [float(entry[3]) for entry in klines]
                    close = [float(entry[4]) for entry in klines]
                    volume = [float(entry[5]) for entry in klines]
                    high = np.asarray(high)
                    low = np.asarray(low)
                    close = np.asarray(close)
                    volume = np.asarray(volume)
                    high = np.delete(high, len(high)-1,0)
                    low = np.delete(low, len(low)-1,0)
                    close = np.delete(close, len(close)-1,0)
                    volume = np.delete(volume, len(volume)-1,0)
                    volume = volume[-10:]
                    lastcloseprice = close[-1]
                    slowk, slowd = talib.STOCH(high, low, close, fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
                    upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                    last_upper = upper[-1]
                    last_lower = lower[-1]
                    last_slowk = slowk[-1]
                    last_slowd = slowd[-1]
                    difuplow = last_upper - last_lower
                    persentage = difuplow / priceNow * 100
                    print(symbol)
                    #STOCH
                    # if last_slowk < 20 and  last_slowd < 20 and all(i >= 20 for i in volume):
                    if last_slowk < 20 and  last_slowd < 20 and all(i >= 2 for i in volume):
                        #BB
                        if last_lower > lastcloseprice:
                            # if slowk[-2] < slowd[-2] and  slowk[-1] > slowd[-1] or slowd[-2] < slowk[-2] and  slowd[-1] > slowk[-1]:
                            if time == '1m' and persentage > 1 and persentage < 4:
                                # winsound.Beep(frequency, duration)
                                print("BUY BUY BUY", symbol, time)
                                text = "BUY BUY BUY:" + str(symbol) + str(time)
                                telegramtest.send_message(text, chat)
                                text = "PER:" + str(persentage)
                                telegramtest.send_message(text, chat)
                                #PRIJS WAARVOOR JE GEKOCHT HEB KOMT HIER TE STAAN
                                orderprijs = float(close[-1])
                                breakeven = float(close[-1]) * 1.00075
                                print("Je hebt gekocht voor:", orderprijs)
                                print("Je breakevenlijn is:", breakeven)
                                text = "Je hebt gekocht voor:" + str(orderprijs)
                                telegramtest.send_message(text, chat)
                                text = "Je breakevenlijn is:" + str(breakeven)
                                telegramtest.send_message(text, chat)
                                

                                eerstebod_BTC = btc_balance / 4
                                hoeveelheid = eerstebod_BTC / orderprijs
                                hoeveelheid = round(hoeveelheid, 2)
                                text = "hoeveelheid coins" + str(hoeveelheid)
                                telegramtest.send_message(text, chat)
                                


                                start_time = datetime.datetime.now()
                                inposition = True
                            elif time == '3m' or time == '5m' and persentage > 1 and persentage < 4:
                                # winsound.Beep(frequency, duration)
                                print("BUY BUY BUY", symbol, time)
                                text = "BUY BUY BUY:" + str(symbol) + str(time)
                                telegramtest.send_message(text, chat)
                                text = "PER:" + str(persentage)
                                telegramtest.send_message(text, chat)
                                #PRIJS WAARVOOR JE GEKOCHT HEB KOMT HIER TE STAAN
                                orderprijs = float(close[-1])
                                breakeven = float(close[-1]) * 1.00075
                                print("Je hebt gekocht voor:", orderprijs)
                                print("Je breakevenlijn is:", breakeven)
                                text = "Je hebt gekocht voor:" + str(orderprijs)
                                telegramtest.send_message(text, chat)
                                text = "Je breakevenlijn is:" + str(breakeven)
                                telegramtest.send_message(text, chat)
                                
                                eerstebod_BTC = btc_balance / 4
                                hoeveelheid = eerstebod_BTC / orderprijs
                                hoeveelheid = round(hoeveelheid, 2)
                                text = "hoeveelheid coins" + str(hoeveelheid)
                                telegramtest.send_message(text, chat)

                                start_time = datetime.datetime.now()
                                inposition = True
                            if inposition == True:
                                print("order placed")
                                while inposition == True:
                                    res = requests.get(marketprices)
                                    data = res.json()
                                    priceNow = float(data['lastPrice'])
                                    klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
                                    close = [float(entry[4]) for entry in klines]
                                    close = np.asarray(close)
                                    close = np.delete(close, len(close)-1,0)
                                    lastclosePrice = close[-1]
                                    end_time = datetime.datetime.now()
                                    time_diff = (end_time - start_time)
                                    execution_time = time_diff.total_seconds()
                                    if orderprijs - ((middle[-1] - last_lower) * 1.01) > priceNow:
                                        print("NOG EEN ORDER PLAATSEN")
                                        firstorderprijs = orderprijs
                                        orderprijs = float(close[-1])
                                        breakeven = (firstorderprijs + orderprijs) / 2 * 1.00075
                                        tweedebod_BTC = eerstebod_BTC
                                        eerste_hoeveelheid = tweedebod_BTC / orderprijs
                                        hoeveelheid = round(hoeveelheid, 2)
                                        text = "NOG EEN ORDER: hoeveelheid coins" + str(hoeveelheid)
                                        telegramtest.send_message(text, chat)
                                        text = "NEW BREAKEVEN" + str(breakeven)
                                        telegramtest.send_message(text, chat)
                                        while inposition == True:
                                            start_str1 = '180 minutes ago UTC'
                                            klines = client.get_historical_klines(symbol=symbol, start_str=start_str1 , interval=time)
                                            high = [float(entry[2]) for entry in klines]
                                            low = [float(entry[3]) for entry in klines]
                                            close = [float(entry[4]) for entry in klines]
                                            volume = [float(entry[5]) for entry in klines]
                                            high = np.asarray(high)
                                            low = np.asarray(low)
                                            close = np.asarray(close)
                                            volume = np.asarray(volume)
                                            sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                            print(real, symbol, time)
                                            res = requests.get(marketprices)
                                            data = res.json()
                                            priceNow = float(data['lastPrice'])
                                            if sarpoint[-2] < breakeven and sarpoint[-1] > priceNow:
                                                oldsar = sarpoint[-1]
                                                #PLACE STOP LIMIT BUY op de SAR door sar -2
                                                text = "STOP LIMIT DOOR SAR"
                                                telegramtest.send_message(text, chat)
                                                while inposition == True:
                                                    start_str1 = '180 minutes ago UTC'
                                                    klines = client.get_historical_klines(symbol=symbol, start_str=start_str1 , interval=time)
                                                    high = [float(entry[2]) for entry in klines]
                                                    low = [float(entry[3]) for entry in klines]
                                                    close = [float(entry[4]) for entry in klines]
                                                    volume = [float(entry[5]) for entry in klines]
                                                    high = np.asarray(high)
                                                    low = np.asarray(low)
                                                    close = np.asarray(close)
                                                    volume = np.asarray(volume)
                                                    sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                                    upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                    print(real, symbol, time)
                                                    res = requests.get(marketprices)
                                                    data = res.json()
                                                    priceNow = float(data['lastPrice'])
                                                    #HIERCONTROLEREN OF STOP GEVALLEN IS
                                                    if inposition == True and sarpoint[-1] != oldsar and sarpoint[-2] - sarpoint[-1] > priceNow * 0.0002 and sarpoint[-1] > priceNow: #HIER KOMT IS NOT GEVULD
                                                        if middle[-1] - sarpoint[-1] < priceNow * 0.0015:
                                                            #ZET STOP BUY BOVEN MIDDLE[-1] * 0,0015
                                                            test = 0
                                                        else :  
                                                            oldsar = sarpoint[-1]
                                                            text = "STOP LIMIT DOOR SAR"
                                                            telegramtest.send_message(text, chat)
                                                        #CANCEL ANDERE ORDER EN MAAK NIEWE ORDER OP SAR [-2]
                                                        #SET DEZE OP NIEUWE CONTROLEREN
                                                    elif priceNow >  sarpoint[-2]: #HIER KOMT ALS STOP IS GEVULD
                                                        OCO = 1 #HIER KMT OCO ORDER met 0,5 winst en 0,5 verlies
                                                        #ALS OCO VERLIES STOP LIMIT ONDER 0,5 % 
                                                        #ALS OCO WINST IS STOP LIMIT ONDER 1 %
                                                        #if pricenow > breakeven * 0.0002:
                                                        #DRIEKWART UITSTAPPEN
                                                        text = "STOP MET DE SAR OP" + str(priceNow)
                                                        telegramtest.send_message(text, chat)
                                                        inposition = False
           
                                    elif priceNow > breakeven * 1.0002 and execution_time > 3600:
                                        #STOP LIMIT
                                        print("SELL SELL SELL EVERYTHING", symbol, time) # EVERYTHING
                                        totaalverkocht = priceNow * hoeveelheid
                                        winst = ((btc_balance + totaalverkocht) - btc_balance) / btc_balance * 100
                                        btc_balance = btc_balance + totaalverkocht
                                        # balance = client.get_asset_balance(asset='BTC')

                                        print("je hebt verkocht voor:", priceNow, "dat is:", winst)
                                        text = "je hebt verkocht voor: " +  str(priceNow) + "dat is: " + str(winst)
                                        telegramtest.send_message(text, chat)
                                        text = "Nieuw balance: " +  str(btc_balance)
                                        telegramtest.send_message(text, chat)
                                        inposition = False
                                    elif priceNow > middle[-1] * 0.9985 and time == '1m':
                                        print("SELL SELL SELL EVERYTHING", symbol, time) # EVERYTHING
                                        totaalverkocht = priceNow * hoeveelheid
                                        winst = ((btc_balance + totaalverkocht) - btc_balance) / btc_balance * 100
                                        btc_balance = btc_balance + totaalverkocht
                                        # balance = client.get_asset_balance(asset='BTC')

                                        print("je hebt verkocht voor:", priceNow, "dat is:", winst)
                                        text = "je hebt verkocht voor: " +  str(priceNow) + "dat is: " + str(winst)
                                        telegramtest.send_message(text, chat)
                                        text = "Nieuw balance: " +  str(btc_balance)
                                        inposition = False
                                    elif priceNow > middle[-1] * 0.9985 and time != '1m':
                                        print("SELL SELL SELL 3 KWART", symbol, time) #3 KWART
                                        text = "Gaat door met 3kwart"
                                        telegramtest.send_message(text, chat)
                                        # inposition = False
                                        while inposition == True:
                                            klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
                                            close = [float(entry[4]) for entry in klines]
                                            close = np.asarray(close)
                                            close = np.delete(close, len(close)-1,0)
                                            upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                            #STOP LOSE ON ORDERPRIJS
                                            if close[-1] > middle[-1]:
                                                #inposition = False
                                                #STOP LOSE ONDER BB MIDDELSTE LIJN
                                                ouwestoplos = middle[-1] * 0.9985
                                                text = "STOP LOSS ONDER MIDDELSTE BB" + str(middle[-1] * 0.9985)
                                                telegramtest.send_message(text, chat)
                                                while inposition == True:
                                                    klines = client.get_historical_klines(symbol=symbol, start_str=start_str , interval=time)
                                                    close = [float(entry[4]) for entry in klines]
                                                    close = np.asarray(close)
                                                    close = np.delete(close, len(close)-1,0)
                                                    upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                    # Alleen voor het testen
                                                    res = requests.get(marketprices)
                                                    data = res.json()
                                                    priceNow = float(data['lastPrice'])
                                                    #if stoploseniet and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                    if priceNow >  ouwestoplos and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                        ouwestoplos = close [-2]
                                                        #CANCELSTOPLOS
                                                        #STOPLOSE
                                                        text = "NIEUWE STOP LOSE" + str(close [-2] * 0.9985)
                                                        telegramtest.send_message(text, chat)
                                                    elif priceNow <  ouwestoplos:
                                                        text = "We zijn uit de trade"
                                                        telegramtest.send_message(text, chat)
                                                        inposition = False