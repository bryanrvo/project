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
from decimal import Decimal

# text, chat = telegramtest.get_last_chat_id_and_text(telegramtest.get_updates())
chat = 1702054190
text = 'start'
telegramtest.send_message(text, chat)

nutijd = datetime.datetime.now()
start_time = nutijd.replace(hour=7, minute=0, second=0, microsecond=0)
end_time = nutijd.replace(hour=23, minute=59, second=0, microsecond=0) 



client = Client(api_key, api_secret)
inposition = False
start_str = '100 minutes ago UTC'

symbols = ['ZRXBTC','ZILBTC','ZENBTC','ZECBTC','YOYOBTC','YFIIBTC','YFIBTC','XVSBTC','XVGBTC','XTZBTC','XRPBTC','XMRBTC','XLMBTC','XEMBTC','WTCBTC','WRXBTC','WPRBTC','WNXMBTC','WINGBTC','WBTCBTC','WAVESBTC','WANBTC','WABIBTC','VITEBTC','VIDTBTC','VIBBTC','VIABTC','VETBTC','UTKBTC','UNIBTC','UNFIBTC','TWTBTC','TVKBTC','TRXBTC','TRUBTC','TROYBTC','TRBBTC','TOMOBTC','THETABTC','TFUELBTC','TCTBTC','SYSBTC','SXPBTC','SUSHIBTC','SUSDBTC','SUNBTC','STXBTC','STRAXBTC','STPTBTC','STORJBTC','STMXBTC','STEEMBTC','SRMBTC','SOLBTC','SNXBTC','SNTBTC','SNMBTC','SNGLSBTC','SKYBTC','SKLBTC','SFPBTC','SCRTBTC','SCBTC','SANDBTC','RVNBTC','RUNEBTC','RSRBTC','ROSEBTC','RLCBTC','RIFBTC','REQBTC','REPBTC','RENBTCBTC','RENBTC','REEFBTC','RDNBTC','RCNBTC','RAMPBTC','QTUMBTC','QSPBTC','QLCBTC','QKCBTC','PSGBTC','PPTBTC','POWRBTC','PONDBTC','POLYBTC','POABTC','PNTBTC','PIVXBTC','PHBBTC','PHABTC','PERPBTC','PERLBTC','PAXGBTC','OXTBTC','OSTBTC','ORNBTC','ONTBTC','ONGBTC','ONEBTC','OMGBTC','OMBTC','OGNBTC','OGBTC','OCEANBTC','OAXBTC','NXSBTC','NULSBTC','NMRBTC','NKNBTC','NEOBTC','NEBLBTC','NEARBTC','NBSBTC','NAVBTC','NASBTC','NANOBTC','MTLBTC','MTHBTC','MKRBTC','MITHBTC','MDTBTC','MDABTC','MATICBTC','MANABTC','LUNABTC','LTOBTC','LTCBTC','LSKBTC','LRCBTC','LOOMBTC','LITBTC','LINKBTC','LINABTC','KSMBTC','KNCBTC','KMDBTC','KAVABTC','JUVBTC','JSTBTC','IRISBTC','IOTXBTC','IOTABTC','IOSTBTC','INJBTC','IDEXBTC','ICXBTC','HNTBTC','HIVEBTC','HBARBTC','HARDBTC','GXSBTC','GVTBTC','GTOBTC','GRTBTC','GRSBTC','GOBTC','GLMBTC','GASBTC','FXSBTC','FUNBTC','FTTBTC','FTMBTC','FRONTBTC','FORBTC','FLMBTC','FISBTC','FIROBTC','FIOBTC','FILBTC','FETBTC','EVXBTC','ETHBTC','ETCBTC','EOSBTC','ENJBTC','ELFBTC','EGLDBTC','EASYBTC','DUSKBTC','DREPBTC','DOTBTC','DOGEBTC','DODOBTC','DOCKBTC','DNTBTC','DLTBTC','DIABTC','DGBBTC','DEGOBTC','DCRBTC','DATABTC','DASHBTC','CVCBTC','CTXCBTC','CTSIBTC','CTKBTC','CRVBTC','COTIBTC','COSBTC','COMPBTC','CNDBTC','CKBBTC','CHZBTC','CHRBTC','CELRBTC','CELOBTC','CDTBTC','CAKEBTC','BZRXBTC','BTSBTC','BTGBTC','BTCSTBTC','BRDBTC','BQXBTC','BNTBTC','BLZBTC','BELBTC','BEAMBTC','BCHBTC','BCDBTC','BATBTC','BANDBTC','BALBTC','BADGERBTC','AXSBTC','AVAXBTC','AVABTC','AUDIOBTC','AUCTIONBTC','ATOMBTC','ATMBTC','ASTBTC','ASRBTC','ARPABTC','ARKBTC','ARDRBTC','APPCBTC','ANTBTC','ANKRBTC','AMBBTC','ALPHABTC','ALICEBTC','ALGOBTC','AKROBTC','AIONBTC','AGIBTC','AERGOBTC','ADXBTC','ADABTC','ACMBTC','AAVEBTC','1INCHBTC']
times = ['1m', '3m', '5m']

nuopditmoment = client.get_asset_balance(asset='BTC')
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
    return high, low, close, volume

def buyfunc(symbol, hoeveelheid, orderprijs):
    order = client.order_limit_buy(symbol=symbol,quantity=hoeveelheid,price=str(orderprijs))
    clientOrderId = order['orderId']
    tm.sleep(3)
    orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
    orderstatus = orderstatus['status']
    if orderstatus == 'REJECTED' or orderstatus == 'REJECTED' or orderstatus == 'CANCELED' or orderstatus == 'PENDING_CANCEL':
        inposition = False
    elif orderstatus == "NEW" or orderstatus == "PARTIALLY_FILLED":
        start_time = datetime.datetime.now()
        while orderstatus != "FILLED":
            orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
            orderstatus = orderstatus['status']
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
                    orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
                    orderstatus = orderstatus['status']
                chat = 1702054190
                text = "gecanceld"
                telegramtest.send_message(text, chat)
            elif orderstatus == "PARTIALLY_FILLED" and execution_time > tijd:
                inposition = True
                orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
                hoeveelheidintrade = float(orderstatus['executedQty'])
                totalpaidfirsttrade =  hoeveelheidintrade * priceNow
    if orderstatus == "FILLED":
        inposition = True
        orderstatus = client.get_order(symbol=symbol,orderId=clientOrderId)
        hoeveelheidintrade = float(orderstatus['executedQty'])
        totalpaidfirsttrade =  hoeveelheidintrade * priceNow
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
    # if orderprijs < 0.0001:
    #     orderprijs = f"{orderprijs:.8f}"
    #     hoeveelheid = round(hoeveelheid)
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


while True:
    if nutijd > start_time and nutijd < end_time and datetime.datetime.today().weekday() < 9:
        for symbol in symbols:
            if symbol == "ZRXBTC":
                print(symbol)
            elif symbol == "1INCHBTC":
                print(symbol)
            for time in times:
                priceNow, volume = lastpricefunc(symbol)
                if priceNow > 0.0000500 and volume > 150:
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
                    if last_slowk < 20 and  last_slowd < 20 and all(i >= 10 for i in volume):
                        if last_lower > lastcloseprice:
                            priceNow, volume = lastpricefunc(symbol)
                            if priceNow < close[-1] * 1.005 and priceNow > close[-1] * 0.995:
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
                                    singlesymbol = symbol.replace('BTC','')
                                    symbolbalace = client.get_asset_balance(asset=singlesymbol)
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
                                        ################### DEZE MOET ERUIT
                                        order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=inzet)
                                        ###################
                                        sellclientOrderId = order['orderId']
                                        tm.sleep(1)
                                    high, low, close, volume = klinesinfo(symbol, start_str, time, False)
                                    upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                    last_lower = lower[-1]
                                    price = str(round(orderprijs - ((middle[-1] - last_lower) * 0.99), len(str(priceNow)) -2))
                                    order = client.order_limit_buy(symbol=symbol, quantity=symbolbalace, price=price)
                                    firstorderprijs = float(orderprijs)
                                    secondorderprijs = float(price)
                                    firstsechoeveelheid = float(symbolbalace)
                                    orderclientOrderId = order['orderId']
                                    while inposition == True:
                                        priceNow, volume = lastpricefunc(symbol)
                                        high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                        lastclosePrice = close[-1]
                                        end_time = datetime.datetime.now()
                                        time_diff = (end_time - start_time)
                                        execution_time = time_diff.total_seconds()
                                        tm.sleep(3)
                                        orderstatus = client.get_order(symbol=symbol, orderId=sellclientOrderId)
                                        sellorderstatus = orderstatus['status']
                                        orderstatus = client.get_order(symbol=symbol, orderId=orderclientOrderId)
                                        buyorderstatus = orderstatus['status']
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
                                                    high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                    upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                    symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                    symbolbalace = float(symbolbalace['locked'])
                                                    symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                    #STOP LOSE ON ORDERPRIJS
                                                    order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=str(orderprijs), price=str(orderprijs * 0.992))
                                                    clientOrderId = order['orderId']
                                                    tm.sleep(1)
                                                    orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                    orderstatus = orderstatus['status']
                                                    if close[-1] > middle[-1] and orderstatus != "FILLED":
                                                        #STOP LOSE ONDER BB MIDDELSTE LIJN
                                                        oldclientOrderId = clientOrderId
                                                        stoplos = middle[-1] * 0.9985
                                                        order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=str(stoplos), price= str(stoplos * 0.992))
                                                        clientOrderId = order['orderId']
                                                        result = client.cancel_order(symbol=symbol,orderId=oldclientOrderId)
                                                        while inposition == True:
                                                            high, low, close, volume = klinesinfo(symbol, start_str, time, True)
                                                            upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                            orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                            orderstatus = orderstatus['status']
                                                            priceNow, volume = lastpricefunc(symbol)
                                                            if orderstatus!= "FILLED" and orderstatus!= "PARTIALLY_FILLED" and close[-1] > close [-2] and  close[-1] > middle[-1]:
                                                                ouwestoplos = float(close [-2])
                                                                oldclientOrderId = clientOrderId
                                                                order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=str(ouwestoplos), price=str(ouwestoplos * 0.992))
                                                                clientOrderId = order['orderId']
                                                                tm.sleep(1)
                                                                result = client.cancel_order(symbol=symbol,orderId=oldclientOrderId)
                                                            elif orderstatus ==  "FILLED":
                                                                inposition = False
                                                    elif orderstatus ==  "FILLED":
                                                        inposition = False
                                        elif buyorderstatus == "FILLED":
                                            result = client.cancel_order(symbol=symbol,orderId=sellclientOrderId)
                                            tm.sleep(3)
                                            breakeven = ((firstorderprijs * firstsechoeveelheid) + (secondorderprijs * firstsechoeveelheid))/ (firstsechoeveelheid + firstsechoeveelheid)
                                            breakeven = breakeven * 1.002
                                            print(breakeven)
                                            while inposition == True:
                                                priceNow, volume = lastpricefunc(symbol)
                                                start_str1 = '180 minutes ago UTC'
                                                high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                                if sarpoint[-2] < breakeven and sarpoint[-1] > priceNow:
                                                    oldsar = sarpoint[-1]
                                                    #PLACE STOP LIMIT BUY op de SAR door sar -2
                                                    symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                    symbolbalace = float(symbolbalace['locked'])
                                                    symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                    stopprice = round(sarpoint[-2], len(str(priceNow)) -2)
                                                    stopprice = str(stopprice)
                                                    price = round(sarpoint[-2] * 0.992, len(str(priceNow)) -2)
                                                    price = str(price)
                                                    print(sarpoint[-2])
                                                    order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=stopprice, price=price, timeInForce=client.TIME_IN_FORCE_GTC,)
                                                    clientOrderId = order['orderId']
                                                    tm.sleep(3)
                                                    orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                    orderstatus = orderstatus['status']
                                                    while inposition == True:
                                                        start_str1 = '180 minutes ago UTC'
                                                        priceNow, volume = lastpricefunc(symbol)
                                                        high, low, close, volume = klinesinfo(symbol, start_str1, time, False)
                                                        sarpoint = talib.SAR(high, low, acceleration=0.02, maximum=0.2)
                                                        upper, middle, lower = talib.BBANDS(close, 20, 2, 2)
                                                        orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                        orderstatus = orderstatus['status']
                                                        #HIER GEBLEVEN
                                                        if orderstatus != "FILLED" and orderstatus != "PARTIALLY_FILLED" and sarpoint[-1] != oldsar and sarpoint[-2] - sarpoint[-1] > priceNow * 0.0002 and sarpoint[-1] > priceNow: #HIER KOMT IS NOT GEVULD
                                                            if middle[-1] - sarpoint[-1] < priceNow * 0.0015:
                                                                #ZET STOP BUY BOVEN MIDDLE[-1] * 0,0015
                                                                result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                                order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=str(middle[-1] * 0.0015), price=str((middle[-1] * 0.0015) * 0.992))
                                                                clientOrderId = order['orderId']
                                                            else :  
                                                                oldsar = sarpoint[-1]
                                                                result = client.cancel_order(symbol=symbol,orderId=clientOrderId)
                                                                order = client.create_order(symbol=symbol, side=client.SIDE_BUY, type=client.ORDER_TYPE_STOP_LOSS_LIMIT, quantity=symbolbalace, stopPrice=str(SAR [-2]), price=str(SAR [-2] * 0.992))
                                                                clientOrderId = order['orderId']
                                                        elif orderstatus == "FILLED": #HIER KOMT ALS STOP IS GEVULD
                                                            symbolbalace = client.get_asset_balance(asset=singlesymbol)
                                                            symbolbalace = float(symbolbalace['locked'])
                                                            symbolbalace = float(round(symbolbalace, len(str(minimum)) -2))
                                                            pricepaid = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                            pricepaid = float(pricepaid['price'])
                                                            bovenprijs = str(pricepaid['price'] * 1.005)
                                                            stopprijs = str(pricepaid['price'] * 0.995)
                                                            limitprijs = str(pricepaid['price'] * 0.990)
                                                            #HIER KMT OCO ORDER met 0,5 winst en 0,5 verlies
                                                            order= client.order_oco_sell(
                                                                symbol= symbol,                                            
                                                                quantity= symbolbalace,                                            
                                                                price= bovenprijs, #BOVENSTE PRIJS                                           
                                                                stopPrice= stopprijs, #STOP                                           
                                                                stopLimitPrice= limitprijs, #DOOR ONDER
                                                                stopLimitTimeInForce=client.TIME_IN_FORCE_GTC)
                                                            tm.sleep(1)
                                                            first = order['orders'][0]['orderId']
                                                            firsttype = order['orderReports'][0]['type']
                                                            second = order['orders'][1]['orderId']
                                                            secondtype = order['orderReports'][1]['type']
                                                            while inposition == True:
                                                                orderstatus = client.get_order(symbol=symbol, orderId=first)
                                                                firstorderstatus = orderstatus['status']
                                                                orderstatus = client.get_order(symbol=symbol, orderId=second)
                                                                secondorderstatus = orderstatus['status']
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
                                                                        if oco == "VERLIES": 
                                                                            test = 1      
                                                                



                                                        #ALS OCO VERLIES STOP LIMIT ONDER 0,5 % 
                                                        #ALS OCO WINST IS STOP LIMIT ONDER 1 %
                                                        #if pricenow > breakeven * 0.0002:
                                                        #DRIEKWART UITSTAPPEN
                                                        





                                        elif buyorderstatus != "FILLED" and sellorderstatus != "FILLED" and execution_time > 3600 and priceNow > breakeven * 1.0002:
                                            order = client.order_limit_sell(symbol=symbol, quantity=symbolbalace, price=priceNow)
                                            clientOrderId = order['orderId']
                                            tm.sleep(1)
                                            orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                            orderstatus = orderstatus['status']
                                            while orderstatus != "FILLED":
                                                orderstatus = client.get_order(symbol=symbol, orderId=clientOrderId)
                                                orderstatus = orderstatus['status']
                                            result = client.cancel_order(symbol=symbol,orderId=sellclientOrderId)
                                            result = client.cancel_order(symbol=symbol,orderId=orderclientOrderId)
                                            inposition = False
                                   