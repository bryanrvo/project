from binance.client import Client
import datetime as dt
import time
import numpy as np
import requests
import talib
import datetime
import telegramtest

# text, chat = telegramtest.get_last_chat_id_and_text(telegramtest.get_updates())
chat = 1702054190
text = 'start'
telegramtest.send_message(text, chat)

nutijd = datetime.datetime.now()
start_time = nutijd.replace(hour=7, minute=0, second=0, microsecond=0)
end_time = nutijd.replace(hour=22, minute=0, second=0, microsecond=0) 

client = Client('', '')
inposition = False
start_str = '100 minutes ago UTC'

symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BNBBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
times = ['1m', '3m', '5m']

def lastpricefunc(symbol):
    marketprices = 'https://api.binance.com/api/v3/ticker/24hr?symbol=' + symbol
    res = requests.get(marketprices)
    data = res.json()
    volume = float(data['volume'])
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


def buyfunc(symbol, time, priceNow):
    chat = 1702054190
    text = "WORD GEKEKEN NAAR: " + str(symbol) + str(time)
    telegramtest.send_message(text, chat)
    btc_balance = client.get_asset_balance(asset='BTC')
    orderprijs = priceNow
    breakeven = orderprijs * 1.00075
    eerstebod_BTC = btc_balance / 4
    hoeveelheid = eerstebod_BTC / orderprijs
    hoeveelheid = round(hoeveelheid, 2) - 0.01
    order = client.order_limit_buy(
        symbol=symbol,
        quantity=hoeveelheid,
        price=orderprijs)
    data = order.json()
    clientOrderId = data['clientOrderId']
    orderstatus = client.get_order(
        symbol=symbol,
        orderId=clientOrderId)
    data = orderstatus.json()
    orderstatus = data['orderstatus']
    if orderstatus == 'REJECTED' or orderstatus == 'REJECTED' or orderstatus == 'CANCELED' or orderstatus == 'PENDING_CANCEL':
        inposition = False
    elif orderstatus == "NEW" or orderstatus == "PARTIALLY_FILLED":
        start_time = datetime.datetime.now()
        while orderstatus != "FILLED":
            orderstatus = client.get_order(
                symbol=symbol,
                orderId=clientOrderId)
            data = orderstatus.json()
            orderstatus = data['orderstatus']
            end_time = datetime.datetime.now()
            time_diff = (end_time - start_time)
            execution_time = time_diff.total_seconds()
            if time == '1m':
                tijd = 121
            elif time == '3m':
                tijd = 181
            elif time == '5m':
                tijd = 301
            if orderstatus == "NEW" and execution_time > tijd:
                inposition = False
                result = client.cancel_order(
                    symbol=symbol,
                    orderId=clientOrderId)
                while orderstatus == "CANCELED":
                    orderstatus = client.get_order(
                        symbol=symbol,
                        orderId=clientOrderId)
                    data = orderstatus.json()
                    orderstatus = data['orderstatus']
            elif orderstatus == "PARTIALLY_FILLED" and execution_time > tijd:
                inposition = True
                eerste_hoeveelheid = data['executedQty']
    if orderstatus == "FILLED":
        inposition = True
        eerste_hoeveelheid = data['executedQty']
        # eerste_hoeveelheid = client.get_asset_balance(asset=symbol) 
    return inposition, orderprijs, breakeven, eerstebod_BTC


while True:
    if nutijd > start_time and nutijd < end_time and datetime.datetime.today().weekday() < 6:
        for symbol in symbols:
            for time in times:
                priceNow, volume = lastpricefunc(symbol)
                if priceNow > 0.000250 and volume > 200:
                    high, low, close, volume = klinesinfo(symbol, start_str, time, True)
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
                    if last_slowk < 20 and  last_slowd < 20 and all(i >= 20 for i in volume):
                        if last_lower > lastcloseprice:
                            priceNow, volume = lastpricefunc(symbol)
                            if priceNow < close[-1] * 1.005 and priceNow > close[-1] * 0.995:
                                if time == '1m' and persentage > 1 and persentage < 4:
                                    inposition, orderprijs, breakeven, eerstebod_BTC = buyfunc(symbol, time, priceNow)

                                    # text = "WORD GEKEKEN NAAR: " + str(symbol) + str(time)
                                    # telegramtest.send_message(text, chat)
                                    # btc_balance = client.get_asset_balance(asset='BTC')
                                    # orderprijs = priceNow
                                    # breakeven = orderprijs * 1.00075
                                    # eerstebod_BTC = btc_balance / 4
                                    # hoeveelheid = eerstebod_BTC / orderprijs
                                    # hoeveelheid = round(hoeveelheid, 2) - 0.01
                                    # order = client.order_limit_buy(
                                    #     symbol=symbol,
                                    #     quantity=hoeveelheid,
                                    #     price=orderprijs)
                                    # data = order.json()
                                    # clientOrderId = data['clientOrderId']
                                    # orderstatus = client.get_order(
                                    #     symbol=symbol,
                                    #     orderId=clientOrderId)
                                    # data = orderstatus.json()
                                    # orderstatus = data['orderstatus']
                                    # if orderstatus == 'REJECTED' or orderstatus == 'REJECTED' or orderstatus == 'CANCELED' or orderstatus == 'PENDING_CANCEL':
                                    #     inposition = False
                                    # elif orderstatus == "NEW" or orderstatus == "PARTIALLY_FILLED":
                                    #     start_time = datetime.datetime.now()
                                    #     while orderstatus != "FILLED":
                                    #         orderstatus = client.get_order(
                                    #             symbol=symbol,
                                    #             orderId=clientOrderId)
                                    #         data = orderstatus.json()
                                    #         orderstatus = data['orderstatus']
                                    #         end_time = datetime.datetime.now()
                                    #         time_diff = (end_time - start_time)
                                    #         execution_time = time_diff.total_seconds()
                                    #         if time == '1m':
                                    #             tijd = 121
                                    #         elif time == '3m':
                                    #             tijd = 181
                                    #         elif time == '5m':
                                    #             tijd = 301
                                    #         if orderstatus == "NEW" and execution_time > tijd:
                                    #             inposition = False
                                    #             result = client.cancel_order(
                                    #                 symbol=symbol,
                                    #                 orderId=clientOrderId)
                                    #             while orderstatus == "CANCELED":
                                    #                 orderstatus = client.get_order(
                                    #                     symbol=symbol,
                                    #                     orderId=clientOrderId)
                                    #                 data = orderstatus.json()
                                    #                 orderstatus = data['orderstatus']
                                    #         elif orderstatus == "PARTIALLY_FILLED" and execution_time > tijd:
                                    #             inposition = True
                                    #             eerste_hoeveelheid = data['executedQty']
                                    # if orderstatus == "FILLED":
                                    #     inposition = True
                                    #     eerste_hoeveelheid = data['executedQty']
                                    #     # eerste_hoeveelheid = client.get_asset_balance(asset=symbol)        
                                    start_time = datetime.datetime.now()
                                elif time == '3m' or time == '5m' and persentage > 1 and persentage < 4:
                                    #HETZELFDE ALS VORIGE FUNCTIE
                                    TEST = 1
                                if inposition == True:
                                    print("order placed")
                                    text = "GEKOCHT VOOR: " + str(priceNow) + str(symbol) + str(time)
                                    telegramtest.send_message(text, chat)
                                    while inposition == True:
                                        priceNow, volume = lastpricefunc(symbol)
                                        high, low, close, volume = klinesinfo(symbol, start_str, time, True)
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
                                                priceNow, volume = lastpricefunc(symbol)
                                                start_str1 = '180 minutes ago UTC'
                                                high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                                if sarpoint[-2] < breakeven and sarpoint[-1] > priceNow:
                                                    oldsar = sarpoint[-1]
                                                    #PLACE STOP LIMIT BUY op de SAR door sar -2
                                                    text = "STOP LIMIT DOOR SAR"
                                                    telegramtest.send_message(text, chat)
                                                    while inposition == True:
                                                        start_str1 = '180 minutes ago UTC'
                                                        priceNow, volume = lastpricefunc(symbol)
                                                        high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                        sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                                        upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
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
                                                high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                #STOP LOSE ON ORDERPRIJS
                                                if close[-1] > middle[-1]:
                                                    #inposition = False
                                                    #STOP LOSE ONDER BB MIDDELSTE LIJN
                                                    ouwestoplos = middle[-1] * 0.9985
                                                    text = "STOP LOSS ONDER MIDDELSTE BB" + str(middle[-1] * 0.9985)
                                                    telegramtest.send_message(text, chat)
                                                    while inposition == True:
                                                        high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                        upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                        # Alleen voor het testen
                                                        priceNow, volume = lastpricefunc(symbol)
                                                        #if stoploseniet and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                        if priceNow >  ouwestoplos and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                            ouwestoplos = close [-2]
                                                            #CANCELSTOPLOS
                                                            #STOPLOSE
                                                            text = "NIEUWE STOP LOSE" + str(close [-2])
                                                            telegramtest.send_message(text, chat)
                                                        elif priceNow <  ouwestoplos:
                                                            text = "We zijn uit de trade"
                                                            telegramtest.send_message(text, chat)
                                                            inposition = False