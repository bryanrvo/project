api_key = ''
api_secret = ''

from binance.client import Client
import pandas as pd
import datetime as dt
import time as tm
import numpy as np
import requests
import datetime
import telegramtest
from binance.exceptions import BinanceAPIException
from decimal import Decimal
from ta.volatility import BollingerBands
from ta.momentum import StochasticOscillator
from ta.trend import PSARIndicator

# text, chat = telegramtest.get_last_chat_id_and_text(telegramtest.get_updates())
chat = 1702054190
text = 'start'
telegramtest.send_message(text, chat)

client = Client(api_key, api_secret)
inposition = False
start_str = '140 minutes ago UTC'

symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
times = ['1m', '3m', '5m']

nuopditmoment = client.get_asset_balance(asset='BTC')
print(nuopditmoment)
nuopditmoment = float(nuopditmoment['free'])
text = "btc balance: " + str(nuopditmoment)
telegramtest.send_message(text, chat)

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
        del klines[-1]
    return klines, high, low, close, volume

def buyfunc(symbol, hoeveelheid, orderprijs):
    order = client.order_limit_buy(symbol=symbol,quantity=hoeveelheid,price=orderprijs)
    clientOrderId = order['orderId']
    orderstatus = ""
    while orderstatus == "":
        try:
            orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
            orderstatus = orderstatus['status']
        except BinanceAPIException as e:
            print(e)
            tm.sleep(10)
    if orderstatus == 'REJECTED' or orderstatus == 'REJECTED' or orderstatus == 'CANCELED' or orderstatus == 'PENDING_CANCEL':
        inposition = False
    elif orderstatus == "NEW" or orderstatus == "PARTIALLY_FILLED":
        start_time = datetime.datetime.now()
        while orderstatus != "FILLED":
            orderstatus = ""
            while orderstatus == "":
                try:
                    orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
                    orderstatus = orderstatus['status']
                except BinanceAPIException as e:
                    print(e)
                    tm.sleep(10)
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
                result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                while orderstatus != "CANCELED":
                    orderstatus = ""
                    while orderstatus == "":
                        try:
                            orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
                            orderstatus = orderstatus['status']
                        except BinanceAPIException as e:
                            print(e)
                            tm.sleep(10)
                chat = 1702054190
                text = "gecanceld"
                telegramtest.send_message(text, chat)
                return False, 0 
            elif orderstatus == "PARTIALLY_FILLED" and execution_time > tijd:
                inposition = True
                orderstatus = ""
                while orderstatus == "":
                    try:
                        orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                        orderstatus = orderstatus['status']
                    except BinanceAPIException as e:
                        print(e)
                        tm.sleep(10)
                totalpaidfirsttrade = 0
    if orderstatus == "FILLED":
        inposition = True
        orderstatus = ""
        while orderstatus == "":
            try:
                orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                orderstatus = orderstatus['status']
            except BinanceAPIException as e:
                print(e)
                tm.sleep(10)
        totalpaidfirsttrade =  0
    return inposition, totalpaidfirsttrade 

def firstbuyfunc(symbol, time, priceNow, close):
    chat = 1702054190
    text = "WORD GEKEKEN NAAR: " + str(symbol) + str(time)
    telegramtest.send_message(text, chat)
    btc_balance = client.get_asset_balance(asset='BTC')
    btc_balance = float(btc_balance['free'])
    if priceNow > close:
        orderprijs = close
    else :
        orderprijs = close
    breakeven = orderprijs * 1.00075
    eersteinleg = btc_balance / 4
    hoeveelheid = eersteinleg / orderprijs
    info = client.get_symbol_info(symbol)
    minimum = float(info['filters'][2]['minQty'])
    hoeveelheid = float(round(hoeveelheid, len(str(minimum)) -2))
    #LENGTE BEREKENEN VAN MINIMUM
    if len(str(minimum)) > 3:
        hoeveelheid = float(Decimal(str(hoeveelheid)) - Decimal('0.01'))
    elif  len(str(minimum)) == 3:
        hoeveelheid = float(Decimal(str(hoeveelheid)) - Decimal('0.1'))
    if orderprijs < 0.0001:
        orderprijs = f"{orderprijs:.8f}"
        hoeveelheid = round(hoeveelheid)
        chat = 1702054190
        text = "TE GOEDKOOP"
        telegramtest.send_message(text, chat)
        return False, 0, 0, 0, 0
    if minimum > hoeveelheid:
        text = "DIT IS TE DUUR: " + str(symbol) + "MINIMAAL: " + str(minimum) + "JOUW HOEVEELHEID: " + str(hoeveelheid)
        telegramtest.send_message(text, chat)
        inposition = False
        totalpaidfirsttrade = 0
        return inposition, orderprijs, breakeven, totalpaidfirsttrade
    print(time)
    print(minimum)
    print(hoeveelheid)
    print(orderprijs)
    inposition, totalpaidfirsttrade = buyfunc(symbol, hoeveelheid, orderprijs)
    return inposition, orderprijs, breakeven, totalpaidfirsttrade, minimum

def binanceDataFrame(klines):
    df = pd.DataFrame(klines,dtype=float, columns = ('Open Time',
                                                                    'Open',
                                                                    'High',
                                                                    'Low',
                                                                    'Close',
                                                                    'Volume',
                                                                    'Close time',
                                                                    'Quote asset volume',
                                                                    'Number of trades',
                                                                    'Taker buy base asset volume',
                                                                    'Taker buy quote asset volume',
                                                                    'Ignore'))

    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    return df

def BBANDS(klines):
    df = binanceDataFrame(klines)
    indicator_bb = BollingerBands(df["Close"])
    df['bb_bbh'] = indicator_bb.bollinger_hband()
    df['bb_bbm'] = indicator_bb.bollinger_mavg()
    df['bb_bbl'] = indicator_bb.bollinger_lband()
    upper = np.asarray(df['bb_bbh'])
    middle = np.asarray(df['bb_bbm'])
    lower = np.asarray(df['bb_bbl'])
    return upper, middle, lower

def STOCH(klines):
    df = binanceDataFrame(klines)
    Stocha = StochasticOscillator(close=df["Close"],high=df["High"],low=df["Low"])
    slowk = Stocha.stoch_signal()
    slowd = slowk.rolling(3).mean()
    slowk = np.asarray(slowk)
    slowd = np.asarray(slowd)
    return slowk, slowd

def SAR(klines):
    df = binanceDataFrame(klines)
    sarpoint = PSARIndicator(close=df["Close"],high=df["High"],low=df["Low"])
    psar = sarpoint.psar()
    psar = np.asarray(psar)
    return psar

def check_time(time_to_check, on_time, off_time):
    if time_to_check >= on_time and time_to_check <= off_time:
        return True
    return False

def positiefbm():
    klines = client.get_historical_klines(symbol='BTCEUR', start_str='240 minutes ago UTC', interval='1m')
    opent = [float(entry[1]) for entry in klines]
    opent = np.asarray(opent)
    priceNow, volume = lastpricefunc('BTCEUR')
    if priceNow > opent[1] * 0.995:
        klines = client.get_historical_klines(symbol='BTCEUR', start_str='60 minutes ago UTC', interval='1m')
        opent = [float(entry[1]) for entry in klines]
        opent = np.asarray(opent)
        priceNow, volume = lastpricefunc('BTCEUR')
        if priceNow > opent[1]:
            return True
    return False

while True:
    current_time = datetime.datetime.now().time()
    startday = check_time(current_time, datetime.time(5,59,55), datetime.time(6,0))
    startsearch = check_time(current_time, datetime.time(6,0), datetime.time(22,0))
    endday = check_time(current_time, datetime.time(22,59,55), datetime.time(23,0))
    if startday and datetime.datetime.today().weekday() < 9:
    #if datetime.datetime.today().weekday() < 9:
        balancenow = client.get_asset_balance(asset='BTC')
        balancenow = float(balancenow['free'])
        text = "Je balans: " + "Hier komt je coin" + str(balancenow)
        telegramtest.send_message(text, chat)
        doelbalance = balancenow * 1.01
        text = "Doel: " + "Hier komt je coin" + str(doelbalance)
        telegramtest.send_message(text, chat)
    elif endday and datetime.datetime.today().weekday() < 9:
        endbalance = client.get_asset_balance(asset='BTC')
        endbalance = float(endbalance['free'])
        try:
            verschil = balancenow / endbalance * 100
            if balancenow > endbalance:
                text = "Doelbehaald met %: " + "Hier komt je coin" + str(verschil)
                telegramtest.send_message(text, chat)
            if balancenow > endbalance:
                text = "Doel niet gehaald met %: " + "Hier komt je coin" + str(verschil)
                telegramtest.send_message(text, chat)
        except NameError:
            text = "balancenow komt niet voor:"
            telegramtest.send_message(text, chat)
    elif startsearch and datetime.datetime.today().weekday() < 9: 
        print("JA IK GA DOOR DE TIJD HEEN")
        print(inposition)
        for symbol in symbols:
            bm = positiefbm()
            print(bm)
            if bm:
                for time in times:
                    priceNow, volume = lastpricefunc(symbol)
                    if priceNow > 0.0000500 and volume > 150:
                        klines, high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                        volume = volume[-10:]
                        lastcloseprice = close[-1]
                        slowk, slowd = STOCH(klines)
                        upper, middle, lower = BBANDS(klines)
                        print(symbol, time)
                        last_upper = upper[-1]
                        last_lower = lower[-1]
                        last_slowk = slowk[-1]
                        last_slowd = slowd[-1]
                        difuplow = last_upper - last_lower
                        persentage = difuplow / priceNow * 100
                        if last_slowk < 20 and  last_slowd < 20 and all(i >= 10 for i in volume):
                            if last_lower > lastcloseprice:
                                priceNow, volume = lastpricefunc(symbol)
                                if priceNow < close[-1] * 1.005 and priceNow > close[-1] * 0.995:
                                    print(persentage)
                                    if time == '1m' and persentage > 1 and persentage < 4:
                                        btc_balanceold = client.get_asset_balance(asset='BTC')
                                        btc_balanceold = float(btc_balanceold['free'])
                                        inposition, orderprijs, breakeven, hoeveelheidintrade, minimum = firstbuyfunc(symbol, time, priceNow, close[-1])        
                                        start_time = datetime.datetime.now()
                                    elif time == '3m' or time == '5m' and persentage > 1 and persentage < 5:
                                        inposition, orderprijs, breakeven, hoeveelheidintrade, minimum = firstbuyfunc(symbol, time, priceNow, close[-1])        
                                        start_time = datetime.datetime.now()
                                    if inposition == True:
                                        print("order placed")
                                        text = "GEKOCHT VOOR: " + str(orderprijs) + str(symbol) + str(time)
                                        telegramtest.send_message(text, chat)
                                        tm.sleep(60)
                                        singlesymbol = symbol.replace('BTC','')
                                        symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                        print(symbolbalace)
                                        symbolbalace = float(symbolbalace['free'])
                                        symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                        inzet = str(round(middle[-1] * 0.9985, len(str(priceNow)) -2))
                                        if time == '1m':
                                            order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=inzet)
                                            sellclientOrderId = order['orderId']
                                        elif time != '1m':
                                            driekwart = symbolbalace / 4 * 3
                                            driekwart = float(round(driekwart, len(str(minimum)) -2))
                                            # order = client.order_limit_sell(symbol=symbol, quantity=driekwart, price=inzet)
                                            ################################# DEZE MOET ERUIT
                                            helft = symbolbalace / 4 * 2
                                            helft = float(round(helft, len(str(minimum)) -2))
                                            order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=inzet)
                                            ################################
                                            sellclientOrderId = order['orderId']
                                            tm.sleep(60)
                                        klines, high, low, close, volume = klinesinfo(symbol, start_str, time, False)
                                        upper, middle, lower = BBANDS(klines)
                                        last_lower = lower[-1]
                                        price = str(round(orderprijs - ((middle[-1] - last_lower) * 0.99), len(str(priceNow)) -2))
                                        order = client.order_limit_buy(symbol=symbol, quantity=symbolbalace, price=price)
                                        firstorderprijs = float(orderprijs)
                                        secondorderprijs = float(price)
                                        firstsechoeveelheid = float(symbolbalace)
                                        orderclientOrderId = order['orderId']
                                        tm.sleep(60)
                                        while inposition == True:
                                            priceNow, volume = lastpricefunc(symbol)
                                            klines, high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                            lastclosePrice = close[-1]
                                            end_time = datetime.datetime.now()
                                            time_diff = (end_time - start_time)
                                            execution_time = time_diff.total_seconds()
                                            sellorderstatus = ""
                                            while sellorderstatus == "":
                                                try:
                                                    orderstatus = client.get_order(symbol=symbol, orderId=sellclientOrderId)
                                                    sellorderstatus = orderstatus['status']
                                                except BinanceAPIException as e:
                                                    print(e)
                                                    tm.sleep(10)
                                            buyorderstatus = ""
                                            while buyorderstatus == "":
                                                try:
                                                    orderstatus = client.get_order(symbol=symbol, orderId=orderclientOrderId)
                                                    buyorderstatus = orderstatus['status']
                                                except BinanceAPIException as e:
                                                    print(e)
                                                    tm.sleep(10)
                                            is_betweenclose3 = breakeven * 0.997 <= close[-3] <= breakeven * 1.003
                                            is_betweenclose2 = breakeven * 0.997 <= close[-2] <= breakeven * 1.003
                                            is_betweenclose1 = breakeven * 0.997 <= close[-1] <= breakeven * 1.003
                                            if sellorderstatus == "FILLED":
                                                text = 'verkocht' + str(time)
                                                telegramtest.send_message(text, chat)
                                                result = client.cancel_order(symbol=symbol,orderId=orderclientOrderId)
                                                if time == '1m':                                               
                                                    inposition = False
                                                elif time != '1m':
                                                    ############## DEZE MOET ERUIT
                                                    inposition = False
                                                    ##############
                                                    while inposition == True:
                                                        klines, high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                        upper, middle, lower = BBANDS(klines)
                                                        symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                        symbolbalace = float(symbolbalace['free'])
                                                        symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                        stopprice = round(orderprijs, len(str(priceNow)) -2)
                                                        stopprice = str(stopprice)
                                                        price = round(orderprijs * 0.992, len(str(priceNow)) -2)
                                                        price = str(price)
                                                        #STOP LOSE ON ORDERPRIJS
                                                        order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price)
                                                        clientOrderId = order['orderId']
                                                        tm.sleep(60)
                                                        orderstatus = ""
                                                        while orderstatus == "":
                                                            try:
                                                                orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                orderstatus = orderstatus['status']
                                                            except BinanceAPIException as e:
                                                                print(e)
                                                                tm.sleep(10)
                                                        if close[-1] > middle[-1] and orderstatus != "FILLED":
                                                            #STOP LOSE ONDER BB MIDDELSTE LIJN
                                                            stopprice = round(middle[-1] * 0.9985, len(str(priceNow)) -2)
                                                            stopprice = str(stopprice)
                                                            price = round((middle[-1] * 0.9985) * 0.992, len(str(priceNow)) -2)
                                                            price = str(price)
                                                            result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                            order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price)
                                                            clientOrderId = order['orderId']
                                                            while inposition == True:
                                                                klines, high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                                upper, middle, lower = BBANDS(klines)
                                                                orderstatus = ""
                                                                while orderstatus == "":
                                                                    try:
                                                                        orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                        orderstatus = orderstatus['status']
                                                                    except BinanceAPIException as e:
                                                                        print(e)
                                                                        tm.sleep(10)
                                                                priceNow, volume = lastpricefunc(symbol)
                                                                if orderstatus!= "FILLED" and orderstatus!= "PARTIALLY_FILLED" and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                                    result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                                    stopprice = round(close [-2], len(str(priceNow)) -2)
                                                                    stopprice = str(stopprice)
                                                                    price = round(close [-2] * 0.992, len(str(priceNow)) -2)
                                                                    price = str(price)
                                                                    order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price)
                                                                    clientOrderId = order['orderId']
                                                                    tm.sleep(60)
                                                                elif orderstatus ==  "FILLED":
                                                                    inposition = False
                                                        elif orderstatus ==  "FILLED":
                                                            inposition = False
                                            elif buyorderstatus == "FILLED":
                                                text = "TWEEDE ORDER:" + str(symbol) + str(time)
                                                telegramtest.send_message(text, chat)
                                                result = client.cancel_order(symbol=symbol,orderId=sellclientOrderId)
                                                tm.sleep(60)
                                                breakeven = ((firstorderprijs * firstsechoeveelheid) + (secondorderprijs * firstsechoeveelheid))/ (firstsechoeveelheid + firstsechoeveelheid)
                                                breakeven = breakeven * 1.002
                                                print(breakeven)
                                                while inposition == True:
                                                    priceNow, volume = lastpricefunc(symbol)
                                                    start_str1 = '240 minutes ago UTC'
                                                    klines, high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                    sarpoint = SAR(klines)
                                                    if sarpoint[-1] < breakeven and sarpoint[-1] > priceNow:
                                                        oldsar = sarpoint[-1]
                                                        #PLACE STOP LIMIT BUY op de SAR door sar -2
                                                        symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                        symbolbalace = float(symbolbalace['free'])
                                                        symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                        if sarpoint[-1] < middle[-1] and middle[-1] * 0.999 < sarpoint[-1]:
                                                            stopprice = round((middle[-1] * 1.001) * 0.998, len(str(priceNow)) -2)
                                                            stopprice = str(stopprice)
                                                            price = round(middle[-1] * 1.001, len(str(priceNow)) -2)
                                                            price = str(price)
                                                            order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price, timeInForce=client.TIME_IN_FORCE_GTC)
                                                            clientOrderId = order['orderId']
                                                            thirdorderprijs = float(price)
                                                            thirdhoeveelheid = float(symbolbalace)
                                                            orderstatus = ""
                                                        else : 
                                                            stopprice = round(sarpoint[-1], len(str(priceNow)) -2)
                                                            stopprice = str(stopprice)
                                                            price = round(sarpoint[-1] * 1.002, len(str(priceNow)) -2)
                                                            price = str(price)
                                                            print("DOOR SAR: ",sarpoint[-1])
                                                            order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price, timeInForce=client.TIME_IN_FORCE_GTC)
                                                            clientOrderId = order['orderId']
                                                            thirdorderprijs = float(price)
                                                            thirdhoeveelheid = float(symbolbalace)
                                                        orderstatus = ""
                                                        while orderstatus == "":
                                                            try:
                                                                orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                orderstatus = orderstatus['status']
                                                            except BinanceAPIException as e:
                                                                print(e)
                                                                tm.sleep(10)
                                                        while inposition == True:
                                                            start_str1 = '240 minutes ago UTC'
                                                            priceNow, volume = lastpricefunc(symbol)
                                                            klines, high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                            sarpoint = SAR(klines)
                                                            upper, middle, lower = BBANDS(klines)
                                                            orderstatus = ""
                                                            while orderstatus == "":
                                                                try:
                                                                    orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                    orderstatus = orderstatus['status']
                                                                except BinanceAPIException as e:
                                                                    print(e)
                                                                    tm.sleep(10)
                                                            if orderstatus != "FILLED" and orderstatus != "PARTIALLY_FILLED" and sarpoint[-1] != oldsar and sarpoint[-2] - sarpoint[-1] > priceNow * 0.0002 and sarpoint[-1] > priceNow:
                                                                if sarpoint[-1] < middle[-1] and middle[-1] * 0.999 < sarpoint[-1]:
                                                                    oldsar = sarpoint[-1]
                                                                    result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                                    stopprice = round(middle[-1] * 1.001, len(str(priceNow)) -2)
                                                                    stopprice = str(stopprice)
                                                                    price = round((middle[-1] * 1.001) * 1.002, len(str(priceNow)) -2)
                                                                    price = str(price)
                                                                    order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price, timeInForce=client.TIME_IN_FORCE_GTC,)
                                                                    clientOrderId = order['orderId']
                                                                    thirdorderprijs = float(price)
                                                                    thirdhoeveelheid = float(symbolbalace)
                                                                else :  
                                                                    oldsar = sarpoint[-1]
                                                                    result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                                    stopprice = round(sarpoint[-1], len(str(priceNow)) -2)
                                                                    stopprice = str(stopprice)
                                                                    price = round(sarpoint[-1] * 1.002, len(str(priceNow)) -2)
                                                                    price = str(price)
                                                                    order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price, timeInForce=client.TIME_IN_FORCE_GTC)
                                                                    clientOrderId = order['orderId']
                                                                    thirdorderprijs = float(price)
                                                                    thirdhoeveelheid = float(symbolbalace)
                                                            elif orderstatus == "FILLED": #HIER KOMT ALS STOP IS GEVULD
                                                                symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                                # symbolbalace = float(symbolbalace['locked']) / 2
                                                                ##### WEG ####
                                                                symbolbalace = float(symbolbalace['free'])
                                                                symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                                print(symbolbalace)
                                                                pricepaid = ""
                                                                while pricepaid == "":
                                                                    try:
                                                                        pricepaid = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                    except BinanceAPIException as e:
                                                                        print(e)
                                                                        tm.sleep(10)
                                                                breakeven = ((firstorderprijs * firstsechoeveelheid) + (secondorderprijs * firstsechoeveelheid) + (thirdorderprijs * thirdhoeveelheid))/ (firstsechoeveelheid + firstsechoeveelheid + thirdhoeveelheid)
                                                                breakeven = breakeven * 1.002
                                                                if upper[-1] - lower[-1] > priceNow / 100 * 1.5:
                                                                    upper, middle, lower
                                                                    pricepaid = float(pricepaid['price'])
                                                                    bovenprijs = pricepaid * 1.01
                                                                    stopprijs = pricepaid * 0.99
                                                                    limitprijs = stopprijs * 0.995
                                                                    print("HIER")
                                                                else : 
                                                                    pricepaid = float(pricepaid['price'])
                                                                    bovenprijs = pricepaid * 1.005
                                                                    stopprijs = pricepaid * 0.995
                                                                    limitprijs = stopprijs * 0.998
                                                                    print("HIER2")
                                                                text = 'OCO ORDER'
                                                                telegramtest.send_message(text, chat)
                                                                bovenprijs = round(bovenprijs, len(str(priceNow)) -2)
                                                                stopprijs = round(stopprijs, len(str(priceNow)) -2)
                                                                limitprijs = round(limitprijs, len(str(priceNow)) -2)
                                                                stopprijs = str(stopprijs)
                                                                limitprijs = str(limitprijs)
                                                                if bovenprijs > breakeven:
                                                                    bovenprijs = round(breakeven * 0.997, len(str(priceNow)) -2)
                                                                bovenprijs = str(bovenprijs)
                                                                print(pricepaid)
                                                                print(bovenprijs)
                                                                print(limitprijs)
                                                                print(stopprice)
                                                                #HIER KMT OCO ORDER met 0,5 winst en 0,5 verlies
                                                                order= client.order_oco_sell(
                                                                    symbol= symbol,                                            
                                                                    quantity= symbolbalace,                                            
                                                                    price= bovenprijs, #BOVENSTE PRIJS                                           
                                                                    stopPrice= stopprijs, #STOP                                           
                                                                    stopLimitPrice= limitprijs, #DOOR ONDER
                                                                    stopLimitTimeInForce=client.TIME_IN_FORCE_GTC)
                                                                first = order['orders'][0]['orderId']
                                                                firsttype = order['orderReports'][0]['type']
                                                                second = order['orders'][1]['orderId']
                                                                secondtype = order['orderReports'][1]['type']
                                                                while inposition == True:
                                                                    firstorderstatus = ""
                                                                    while firstorderstatus == "":
                                                                        try:
                                                                            orderstatus = client.get_order(symbol=symbol, orderId=first)
                                                                            firstorderstatus = orderstatus['status']
                                                                        except BinanceAPIException as e:
                                                                            print(e)
                                                                            tm.sleep(10)
                                                                    secondorderstatus = ""
                                                                    while secondorderstatus == "":
                                                                        try:
                                                                            orderstatus = client.get_order(symbol=symbol, orderId=second)
                                                                            secondorderstatus = orderstatus['status']
                                                                        except BinanceAPIException as e:
                                                                            print(e)
                                                                            tm.sleep(10)
                                                                    if firstorderstatus == "FILLED" or secondorderstatus == "FILLED":
                                                                        if firstorderstatus == "FILLED":
                                                                            if firsttype == "STOP_LOSS_LIMIT":
                                                                                oco = "VERLIES"
                                                                            elif firsttype == "LIMIT_MAKER":
                                                                                oco = "WINST"
                                                                        elif secondorderstatus == "FILLED":
                                                                            if secondtype == "STOP_LOSS_LIMIT":
                                                                                oco = "VERLIES"
                                                                            elif secondtype == "LIMIT_MAKER":
                                                                                oco = "WINST"
                                                                        while inposition == True:
                                                                            if oco == "WINST":
                                                                                #MEE LIFTEN OP LAATSTE CLOSE
                                                                                #HIER KOMT DE WHILE TRUE LOOP VAN LAST CLOSE
                                                                                #ORDERPRIJS WORD thirdorderprijs
                                                                                text = 'WINST UIT DE OCO ORDER ZELF VERDER GAAN'
                                                                                telegramtest.send_message(text, chat)
                                                                                inposition = False
                                                                            elif oco == "VERLIES":
                                                                                # symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                                                # symbolbalace = float(symbolbalace['free'])
                                                                                # symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                                                # order = client.order_market_sell(symbol=symbol,quantity=symbolbalace)
                                                                                text = 'JE HEBT VERLIES GEMAAKT!'
                                                                                telegramtest.send_message(text, chat)
                                                                                inposition = False
                                                                            
                                                    elif priceNow > breakeven * 1.002:
                                                        tm.sleep(30)
                                                        symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                        symbolbalace = float(symbolbalace['free'])
                                                        symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                        print(symbolbalace)
                                                        order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=str(priceNow))
                                                        clientOrderId = order['orderId']
                                                        orderstatus = ""
                                                        while orderstatus == "":
                                                            try:
                                                                orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                orderstatus = orderstatus['status']
                                                            except BinanceAPIException as e:
                                                                print(e)
                                                                tm.sleep(10)
                                                        while orderstatus != "FILLED":
                                                            orderstatus = ""
                                                            while orderstatus == "":
                                                                try:
                                                                    orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                                    orderstatus = orderstatus['status']
                                                                except BinanceAPIException as e:
                                                                    print(e)
                                                                    tm.sleep(10)
                                                            inposition = False
                                                            #MISSCHIEN 3 KWART


                                                                    

                                                            

                                            elif buyorderstatus != "FILLED" and sellorderstatus != "FILLED" and execution_time > 3600 and priceNow > breakeven * 1.0002 and is_betweenclose1 and is_betweenclose2 and is_betweenclose3:
                                                result = client.cancel_order(symbol=symbol,orderId=sellclientOrderId)
                                                result = client.cancel_order(symbol=symbol,orderId=orderclientOrderId)
                                                tm.sleep(60)
                                                order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=priceNow)
                                                clientOrderId = order['orderId']
                                                tm.sleep(60)
                                                orderstatus = ""
                                                while orderstatus == "":
                                                    try:
                                                        orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                        orderstatus = orderstatus['status']
                                                    except BinanceAPIException as e:
                                                        print(e)
                                                        tm.sleep(10)
                                                while orderstatus != "FILLED":
                                                    orderstatus = ""
                                                    while orderstatus == "":
                                                        try:
                                                            orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                            orderstatus = orderstatus['status']
                                                        except BinanceAPIException as e:
                                                            print(e)
                                                            tm.sleep(10)
                                                result = client.cancel_order(symbol=symbol,orderId=sellclientOrderId)
                                                result = client.cancel_order(symbol=symbol,orderId=orderclientOrderId)
                                                text = "VERKOCHT 1 UUR:" + str(symbol) + str(time)
                                                telegramtest.send_message(text, chat)
                                                inposition = False
                                    
