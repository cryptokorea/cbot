__author__ = 'Charlie Kim'

import my_complete_orders
import my_balance
import my_buy
import my_sell
import my_limit_orders
import my_cancel
import my_market_orders
import time
import datetime
import sys

def buy(price, qty, currency):
    func_name = buy.__name__
    try:
        my_buy.set_price(price)
        my_buy.set_qty(qty)
        my_buy.set_currency(currency)
        ret = my_buy.get_result()
        if ret['errorCode'] == '0':
            print("[OK][BUY]", ret)
        else:
            print("[NOK][BUY]", ret)
        return ret
    except:
        return False

def sell(price, qty, currency):
    func_name = sell.__name__
    try:
        my_sell.set_price(price)
        my_sell.set_qty(qty)
        my_sell.set_currency(currency)
        ret = my_sell.get_result()
        if ret['errorCode'] == '0':
            print("[OK][SELL]", ret)
        else:
            print("[NOK][SELL]", ret)
        return ret
    except:
        return False


def complete_orders(currency):
    func_name = complete_orders.__name__
    try:
        my_complete_orders.set_payload_currency(currency)
        ret = my_complete_orders.get_result()
        if ret['errorCode'] == '0':
            for i in range(len(ret['completeOrders'])):
                orderId = ret['completeOrders'][i]['orderId']
                price = ret['completeOrders'][i]['price']
                qty = ret['completeOrders'][i]['qty']
                type = ret['completeOrders'][i]['type']
                print("[OK][COMPLETE][%s][%s][orderId : %s] price : %s, qty : %s" % (currency, type, orderId, price, qty))
        return ret
    except:
        return False


# open orders
def limit_orders_nok(currency):
    func_name = limit_orders_nok.__name__
    try:
        my_list = {}
        my_limit_orders.set_currency(currency)
        ret = my_limit_orders.get_result()
        # print (ret)
        if ret['errorCode'] == '0' and ret['limitOrders'] != None:
            for i in range(len(ret['limitOrders'])):
                orderId = ret['limitOrders'][i]['orderId']
                price = ret['limitOrders'][i]['price']
                qty = ret['limitOrders'][i]['qty']
                type = ret['limitOrders'][i]['type']
                print("[OK][OPEN][%s][%s][orderId : %s] price : %s, qty : %s" % (currency, type, orderId, price, qty))
                my_list[orderId] = currency, type, price, qty
            return my_list
    except:
        return False

# open orders
def limit_orders(currency):
    func_name = limit_orders.__name__
    try:
        my_limit_orders.set_currency(currency)
        ret = my_limit_orders.get_result()
        #print(ret)
        ret2 = ret['limitOrders']
        #print(ret2)
        if ret['errorCode'] == '0' and len(ret2) > 0:
            bid_count = 0
            ask_count = 0
            for i in range(len(ret2)):
                if ret2[i]['type'] == 'bid':
                    bid_count += 1
                elif ret2[i]['type'] == 'ask':
                    ask_count += 1
            #print("[OK][%s]Total orders : %s" % (currency, len(ret2)))
            #print("[OK][%s]      bid orders : %s" % (currency, bid_count))
            #print("[OK][%s]      ask orders : %s" % (currency, ask_count))
            return ret2
    except:
        return False


# open orders
def limit_orders_old(currency):
    func_name = limit_orders_old.__name__
    try:
        my_limit_orders.set_currency(currency)
        ret = my_limit_orders.get_result()
        return ret
    except:
        return False


# open orders
def all_limit_orders():
    func_name = all_limit_orders.__name__
    my_list = all_currency()
    for i in range(len(my_list)):
        try:
            currency = my_list[i]
            limit_orders(currency)
            time.sleep(1) # MUST sleep to avoid exception
        except:
            print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
            continue
      #  ret = limit_orders(currency)
      #  print (ret)
      #  my_list2.[ret['orderId']] = ret['orderId'], ret['orderId'], ret['orderId'], ret['orderId']

    """"
    for i in range(len(my_list)):
        print(my_list)
        currency = my_list[i]
        print(currency)
        my_list2 = limit_orders(currency)
        print(my_list2)
    """

    """""
    ret = my_limit_orders.get_result()
    print(ret)
    if ret['errorCode'] == '0':
        for i in range(len(ret['limitOrders'])):
            currency = ret['limitOrders'][i]['currency']
            orderId = ret['limitOrders'][i]['orderId']
            price = ret['limitOrders'][i]['price']
            qty = ret['limitOrders'][i]['qty']
            type = ret['limitOrders'][i]['type']
            print("[OK][OPEN][%s][%s][orderId : %s] price : %s, qty : %s" % (currency, type, orderId, price, qty))
            my_list[orderId] = currency, type, price, qty
        return my_list
"""

#{'bch': {'avail': '0.00000000', 'balance': '0.00000000'}, 'qtum': {'avail': '0.00000000', 'balance': '0.00000000'}, 'krw': {'avail': '2458064', 'balance': '12694314'}, 'errorCode': '0', 'etc': {'avail': '0.00000000', 'balance': '0.00000000'}, 'result': 'success', 'btc': {'avail': '0.00000000', 'balance': '0.00000000'}, 'normalWallets': [], 'eth': {'avail': '0.00006647', 'balance': '0.00006647'}, 'xrp': {'avail': '9.98700000', 'balance': '12.98700000'}}
def balance(currency):
    #func_name = func_balance.__name__
    try:
        ret = my_balance.get_result()
        balance = ret[currency]['balance']
        avail = ret[currency]['avail']
        if ret['errorCode'] == '0':
            print("[OK][BALANCE][%s] avail : %s, balance : %s" % (currency, avail, balance))
        else:
            print("[NOK][BALANCE][%s]" % currency, ret)
        return ret[currency]
    except:
        print("[ERR][%s][LINE: %s][FUNC : ?? ]" % (my_time(), sys._getframe().f_lineno)) # TODO
        return

def all_balance():
    func_name = all_balance.__name__
    ret = my_balance.get_result()
    my_list = {}
    if ret['errorCode'] == '0':
        for i in range(len(ret)):
            key = list(ret.keys())[i]
            try:
                avail = ret[key]['avail']
                try:
                    balance = ret[key]['balance']
                except:
                    print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                    continue
            except:
                print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                continue
            if float(avail) > 0 or float(balance) > 0:
                print("[OK][BALANCE][%s] avail : %s, balance : %s" % (key, avail, balance))
                my_list[key] = avail, balance
        return my_list

def all_currency():
    func_name = all_currency.__name__
    ret = my_balance.get_result()
    my_list = []
    if ret['errorCode'] == '0':
        for i in range(len(ret)):
            key = list(ret.keys())[i]
            try:
                avail = ret[key]['avail']
                try:
                    balance = ret[key]['balance']
                except:
                    print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                    continue
            except:
                print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                continue
            my_list.append(key)
        print("[OK][ALL_CUR]", my_list)
    return my_list



""""
  "order_id": "OrderID",
  "price": 500000,
  "qty": 0.1,
  "is_ask": 1,
  "currency": "btc"
"""
def cancel(order_id, price, qty, is_ask, currency):
    func_name = cancel.__name__
    try:
        print("[CHECK][%s] cancel" % currency, order_id, price, qty, is_ask)
        my_cancel.set_order_id(order_id)
        my_cancel.set_price(price)
        my_cancel.set_qty(qty)
        my_cancel.set_is_ask(is_ask)
        my_cancel.set_currency(currency)
        ret = my_cancel.get_result()
        print(ret)
        return True
    except:
        return False


def cancel_bids(currency):
    func_name = cancel_bids.__name__
    try:
        ret = limit_orders(currency)
        if ret == None:
            return
        print(ret)
        for i in range(len(ret)):
            orderId = ret[i]['orderId']
            price = ret[i]['price']
            qty = ret[i]['qty']
            if ret[i]['type'] == 'ask':
                is_ask = 1
            else:
                is_ask = 0
            if is_ask == 0:
                cancel(orderId, price, qty, is_ask, currency)
            else:
                return
    except:
        return False



def cancel_asks(currency):
    func_name = cancel_asks.__name__
    ret = limit_orders(currency)
    if ret == None:
        return
    print(ret)
    for i in range(len(ret)):
        orderId = ret[i]['orderId']
        price = ret[i]['price']
        qty = ret[i]['qty']
        if ret[i]['type'] == 'ask':
            is_ask = 1
        else:
            is_ask = 0
        if is_ask == 1:
            cancel(orderId, price, qty, is_ask, currency)
        else:
            return

def cancel_all(currency):
    func_name = cancel_all.__name__
    try:
        ret = limit_orders(currency)
        if ret == None:
            return
        for i in range(len(ret)):
            orderId = ret[i]['orderId']
            price = ret[i]['price']
            qty = ret[i]['qty']
            if ret[i]['type'] == 'ask':
                is_ask = 1
            else:
                is_ask = 0
            cancel(orderId, price, qty, is_ask, currency)
    except:
        return False



def market_orders(currency):
    func_name = market_orders.__name__
    for i in range(3):
        try:
            ret = my_market_orders.get_result(currency)
            if ret != False:
                print("[CHECK][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                print(ret)
                return ret
            else:
                print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
                time.sleep(1)
                continue
        except:
            print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
            continue





def highest_market_bid(currency):
    func_name = highest_market_bid.__name__
    try:
        ret = market_orders(currency)
        print("[CHECK][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name), ret)
        ret2 = ret['bid'][0]['price']
        return ret2
    except:
        print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
        return False




def highest_market_ask(currency):
    func_name = highest_market_ask.__name__
    try:
        ret = market_orders(currency)
        ret2 = ret['ask'][0]['price']
        return ret2
    except:
        print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_time(), sys._getframe().f_lineno, func_name))
        return False

def my_line_no():
    ret = sys._getframe().f_lineno
    return ret

def my_line_no2():
    ret = sys._getframe().f_lineno
    ts = time.time()
    ts2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return ts2, ret

def my_time():
    ts = time.time()
    ts2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return ts2


        #   ret = {"timestamp":"1506698236","bid":[{"price":"219","qty":"244005.4030"},{"price":"218","qty":"299948.4597"},{"price":"217","qty":"565307.0783"},{"price":"216","qty":"436540.0643"},{"price":"215","qty":"428040.4877"},{"price":"214","qty":"332126.8169"},{"price":"213","qty":"355733.3890"},{"price":"212","qty":"506473.9621"},{"price":"211","qty":"250972.7863"},{"price":"210","qty":"329717.9923"},{"price":"209","qty":"427351.8230"},{"price":"208","qty":"179244.4648"},{"price":"207","qty":"120262.1883"},{"price":"206","qty":"51386.3938"},{"price":"205","qty":"228936.7556"},{"price":"204","qty":"218596.4918"},{"price":"203","qty":"24547.8715"},{"price":"202","qty":"105381.9316"},{"price":"201","qty":"400864.2366"},{"price":"200","qty":"444515.9005"},{"price":"199","qty":"151382.2018"},{"price":"198","qty":"285932.1056"},{"price":"197","qty":"256215.8071"},{"price":"196","qty":"176524.3385"},{"price":"195","qty":"337019.1840"},{"price":"194","qty":"168415.5184"},{"price":"193","qty":"532662.6368"},{"price":"192","qty":"40194.9300"},{"price":"191","qty":"18922.3560"},{"price":"190","qty":"508294.5349"},{"price":"189","qty":"137365.8991"},{"price":"188","qty":"90634.4664"},{"price":"187","qty":"287703.5400"},{"price":"186","qty":"18594.3887"},{"price":"185","qty":"402030.6209"},{"price":"184","qty":"255199.7873"},{"price":"183","qty":"297231.5080"},{"price":"182","qty":"168772.3881"},{"price":"181","qty":"14146.7015"},{"price":"180","qty":"808123.8161"},{"price":"179","qty":"52594.0502"},{"price":"178","qty":"194710.5080"},{"price":"177","qty":"178031.1298"},{"price":"176","qty":"39029.4977"},{"price":"175","qty":"172695.9136"},{"price":"174","qty":"73956.8042"},{"price":"173","qty":"161883.2075"},{"price":"172","qty":"90366.0290"},{"price":"171","qty":"278028.9530"},{"price":"170","qty":"636202.7466"},{"price":"169","qty":"71668.2016"},{"price":"168","qty":"40972.6487"},{"price":"167","qty":"134808.9112"},{"price":"166","qty":"273476.0000"},{"price":"165","qty":"275750.6757"},{"price":"164","qty":"47043.7317"},{"price":"163","qty":"137069.5593"},{"price":"162","qty":"118248.7283"},{"price":"161","qty":"15509.1129"},{"price":"160","qty":"336871.6691"},{"price":"159","qty":"6039.0011"},{"price":"158","qty":"29764.3037"},{"price":"157","qty":"34951.0011"},{"price":"156","qty":"101065.9871"},{"price":"155","qty":"12160.8526"},{"price":"154","qty":"16090.0600"},{"price":"153","qty":"8100.2960"},{"price":"152","qty":"38360.2631"},{"price":"151","qty":"59674.6434"},{"price":"150","qty":"355780.4105"},{"price":"149","qty":"1361.0011"},{"price":"148","qty":"770.0000"},{"price":"147","qty":"1267.0011"},{"price":"146","qty":"410.0000"},{"price":"145","qty":"3543.6563"},{"price":"144","qty":"590.0000"},{"price":"143","qty":"1546.1969"},{"price":"142","qty":"680.0000"},{"price":"141","qty":"1344.0011"},{"price":"140","qty":"123673.0436"},{"price":"139","qty":"1774.0011"},{"price":"138","qty":"51025.0000"},{"price":"137","qty":"62242.3946"},{"price":"136","qty":"350.0000"},{"price":"135","qty":"60841.1110"},{"price":"134","qty":"1660.0000"},{"price":"133","qty":"11976.0000"},{"price":"132","qty":"343.0000"},{"price":"131","qty":"19514.3969"},{"price":"130","qty":"111572.4700"},{"price":"129","qty":"16264.0000"},{"price":"128","qty":"2260.0000"},{"price":"127","qty":"102386.4251"},{"price":"126","qty":"11954.4761"},{"price":"125","qty":"252797.0260"},{"price":"124","qty":"10311.8145"},{"price":"123","qty":"503265.0162"},{"price":"122","qty":"310.0000"},{"price":"121","qty":"73495.7024"},{"price":"120","qty":"303924.1090"},{"price":"119","qty":"200.0000"},{"price":"118","qty":"6410.0000"},{"price":"117","qty":"200.0000"},{"price":"116","qty":"210.0000"},{"price":"115","qty":"36446.5565"},{"price":"114","qty":"210.0000"},{"price":"113","qty":"1220.0000"},{"price":"112","qty":"200.0000"},{"price":"111","qty":"220.0000"},{"price":"110","qty":"50540.4737"},{"price":"109","qty":"4714.5221"},{"price":"107","qty":"5000.0000"},{"price":"105","qty":"1000.0000"},{"price":"104","qty":"1121.0000"},{"price":"102","qty":"4000.0000"},{"price":"101","qty":"2000.0000"},{"price":"100","qty":"392499.4611"},{"price":"99","qty":"4135.1919"},{"price":"98","qty":"5100.0000"},{"price":"97","qty":"4473.9484"},{"price":"96","qty":"3131.2604"},{"price":"95","qty":"2600.0000"},{"price":"92","qty":"1000.0000"},{"price":"90","qty":"22.0000"},{"price":"85","qty":"200.0000"},{"price":"82","qty":"3500.0000"},{"price":"75","qty":"3884.0000"},{"price":"73","qty":"1.0000"},{"price":"50","qty":"12000.0000"},{"price":"45","qty":"28.0000"},{"price":"25","qty":"5000.0000"},{"price":"20","qty":"1501.0000"},{"price":"19","qty":"1.0526"},{"price":"12","qty":"1.0000"},{"price":"10","qty":"191120.0000"},{"price":"6","qty":"1.0000"},{"price":"5","qty":"49000.2000"},{"price":"3","qty":"463290.3333"},{"price":"2","qty":"1000001.0000"},{"price":"1","qty":"1701396.0000"}],"errorCode":"0","currency":"xrp","result":"success","ask":[{"price":"220","qty":"99784.9871"},{"price":"221","qty":"945514.0879"},{"price":"222","qty":"833887.1416"},{"price":"223","qty":"169704.0423"},{"price":"224","qty":"57079.0720"},{"price":"225","qty":"171844.4709"},{"price":"226","qty":"243516.3984"},{"price":"227","qty":"295394.6318"},{"price":"228","qty":"260079.7159"},{"price":"229","qty":"90772.6982"},{"price":"230","qty":"728279.0360"},{"price":"231","qty":"492874.0620"},{"price":"232","qty":"425910.4519"},{"price":"233","qty":"220786.8754"},{"price":"234","qty":"283123.6917"},{"price":"235","qty":"513062.1408"},{"price":"236","qty":"190620.8888"},{"price":"237","qty":"271821.4270"},{"price":"238","qty":"930004.7146"},{"price":"239","qty":"712695.6919"},{"price":"240","qty":"709818.4435"},{"price":"241","qty":"400925.5558"},{"price":"242","qty":"94134.5095"},{"price":"243","qty":"386482.4868"},{"price":"244","qty":"218815.8030"},{"price":"245","qty":"1580670.7515"},{"price":"246","qty":"1385824.8952"},{"price":"247","qty":"1341920.5323"},{"price":"248","qty":"1317009.1944"},{"price":"249","qty":"1176739.3252"},{"price":"250","qty":"2388140.6579"},{"price":"251","qty":"1493514.9155"},{"price":"252","qty":"1120144.1562"},{"price":"253","qty":"1153945.1790"},{"price":"254","qty":"755840.1529"},{"price":"255","qty":"2373819.2408"},{"price":"256","qty":"125839.4084"},{"price":"257","qty":"425977.3246"},{"price":"258","qty":"601670.7119"},{"price":"259","qty":"223736.5631"},{"price":"260","qty":"845537.1933"},{"price":"261","qty":"189714.0824"},{"price":"262","qty":"118365.1099"},{"price":"263","qty":"159034.9386"},{"price":"264","qty":"168667.9915"},{"price":"265","qty":"1355280.4280"},{"price":"266","qty":"25626.5396"},{"price":"267","qty":"51234.8439"},{"price":"268","qty":"55190.9625"},{"price":"269","qty":"122033.5598"},{"price":"270","qty":"473994.7404"},{"price":"271","qty":"42857.2108"},{"price":"272","qty":"75383.7133"},{"price":"273","qty":"72008.5342"},{"price":"274","qty":"191749.6424"},{"price":"275","qty":"1305910.2437"},{"price":"276","qty":"257192.4167"},{"price":"277","qty":"40728.9083"},{"price":"278","qty":"543618.3931"},{"price":"279","qty":"196468.2375"},{"price":"280","qty":"653674.2024"},{"price":"281","qty":"112063.0235"},{"price":"282","qty":"490289.2274"},{"price":"283","qty":"43550.1836"},{"price":"284","qty":"172333.2851"},{"price":"285","qty":"537843.3740"},{"price":"286","qty":"122727.4741"},{"price":"287","qty":"112225.2310"},{"price":"288","qty":"270543.0895"},{"price":"289","qty":"469492.7767"},{"price":"290","qty":"796149.6729"},{"price":"291","qty":"147441.3959"},{"price":"292","qty":"107061.1987"},{"price":"293","qty":"424306.1865"},{"price":"294","qty":"107617.9018"},{"price":"295","qty":"575811.6295"},{"price":"296","qty":"48766.9685"},{"price":"297","qty":"130825.0895"},{"price":"298","qty":"265348.7516"},{"price":"299","qty":"514495.0380"},{"price":"300","qty":"1720693.4347"},{"price":"301","qty":"262155.9069"},{"price":"302","qty":"87471.9986"},{"price":"303","qty":"143300.8438"},{"price":"304","qty":"125040.0230"},{"price":"305","qty":"454382.8006"},{"price":"306","qty":"22543.9436"},{"price":"307","qty":"72874.7345"},{"price":"308","qty":"161656.2741"},{"price":"309","qty":"130040.6730"},{"price":"310","qty":"742886.9501"},{"price":"311","qty":"85200.2612"},{"price":"312","qty":"411855.3654"},{"price":"313","qty":"72303.5106"},{"price":"314","qty":"64265.8132"},{"price":"315","qty":"536872.1068"},{"price":"316","qty":"94954.5589"},{"price":"317","qty":"53310.2690"},{"price":"318","qty":"94665.4863"},{"price":"319","qty":"150790.8989"},{"price":"320","qty":"2199991.2717"},{"price":"321","qty":"197378.6326"},{"price":"322","qty":"200525.7024"},{"price":"323","qty":"408888.5218"},{"price":"324","qty":"408260.3401"},{"price":"325","qty":"808930.1239"},{"price":"326","qty":"98859.6727"},{"price":"327","qty":"137745.4289"},{"price":"328","qty":"330477.8738"},{"price":"329","qty":"143256.8220"},{"price":"330","qty":"2881788.1898"},{"price":"331","qty":"251954.0313"},{"price":"332","qty":"55498.2943"},{"price":"333","qty":"1546425.1194"},{"price":"334","qty":"151015.8452"},{"price":"335","qty":"511668.5100"},{"price":"336","qty":"110836.3440"},{"price":"337","qty":"74835.4092"},{"price":"338","qty":"2705502.3054"},{"price":"339","qty":"171671.5861"},{"price":"340","qty":"832090.9925"},{"price":"341","qty":"59875.0556"},{"price":"342","qty":"138230.1941"},{"price":"343","qty":"86971.5625"},{"price":"344","qty":"56410.9893"},{"price":"345","qty":"518898.3327"},{"price":"346","qty":"100855.0521"},{"price":"347","qty":"298049.1173"},{"price":"348","qty":"547866.0249"},{"price":"349","qty":"476496.9692"},{"price":"350","qty":"2133563.9100"},{"price":"351","qty":"68202.0456"},{"price":"352","qty":"364178.9667"},{"price":"353","qty":"58566.7311"},{"price":"354","qty":"39991.8237"},{"price":"355","qty":"399301.2324"},{"price":"356","qty":"66443.6269"},{"price":"357","qty":"110680.4572"},{"price":"358","qty":"63706.0270"},{"price":"359","qty":"147995.3637"},{"price":"360","qty":"636096.1910"},{"price":"361","qty":"104333.3289"},{"price":"362","qty":"19335.1424"},{"price":"363","qty":"31237.6918"},{"price":"364","qty":"32654.7418"},{"price":"365","qty":"298103.0331"},{"price":"366","qty":"40316.2729"},{"price":"367","qty":"32139.0323"},{"price":"368","qty":"88907.3456"},{"price":"369","qty":"87218.6948"},{"price":"370","qty":"503626.6753"}]}
 #   ret2 = ret['bid'][0]['price']
 #   print(ret)
 #   print(ret2)



"""
a = 1
b = 12
c = 123
d = 1234
e = 12345  # 12340               #
f = 123456  # 123400
g = 1234567  # 1,234,000
h = 12345678  # 12,340,000
i = 123456789 # 123,400,000
"""
def coinone_krw(price):
    ret = len(str(price))
    if ret <= 4:
        return price
    else:
        ret -= 4
    val = 10 ** ret
    ret2 = int(price) / val * val
    return str(ret2)


# 0.01998 --> 0.01
def coinone_qty(qty):
    ret = round(float(qty), 2)
    if ret < 0.1:
        ret -= 0.01
    elif ret < 0.01:
        return 0
    else:
        return str(ret)







#def cointone_qty(qty):



if __name__ == "__main__":
    # return : {'errorCode': '0', 'orderId': '03e287ff-e6f1-4bb0-8b7f-ad1e304f27e8', 'result': 'success'})
    # buy('100', '1', 'xrp')

    # return : {'errorCode': '0', 'orderId': '6e17798c-dad8-46c6-988a-3268ddc0e31c', 'result': 'success'})
    # sell('300', '1', 'xrp') #

    # return : {'avail': '2458064', 'balance': '12694314'}
    # balance('krw') #

    # return : # {'eth': ('0.00006647', '0.00006647'), 'krw': ('2458064', '12694314'), 'xrp': ('9.98700000', '12.98700000')}
    #all_balance()

    # return : {'errorCode': '0', 'completeOrders': [{'orderId': 'C19E4E6A-3BDC-4AC9-BC01-6405C5592B5F', 'fee': '0.01000000', 'timestamp': '1506172465', 'price': '199', 'qty': '10.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '2F95CB37-217C-42EC-9008-1AF6680B6797', 'fee': '0.00100000', 'timestamp': '1506169889', 'price': '201', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '7F76B19F-28CB-46C0-AA0D-976DA4814BB0', 'fee': '0.00100000', 'timestamp': '1506169646', 'price': '200', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': 'C122AA29-AE49-4B85-9165-A1547F90A91B', 'fee': '0.00100000', 'timestamp': '1506169609', 'price': '200', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}], 'result': 'success'}
    # complete_orders('xrp')

    # return : [{'orderId': '4efa30cd-449c-4bd5-9133-650703a6f453', 'index': '0', 'timestamp': '1506183720', 'price': '100', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '6e17798c-dad8-46c6-988a-3268ddc0e31c', 'index': '0', 'timestamp': '1506182777', 'price': '300', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'ask'}, {'orderId': '03e287ff-e6f1-4bb0-8b7f-ad1e304f27e8', 'index': '1', 'timestamp': '1506182777', 'price': '100', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': 'f5808d32-e371-4f38-802f-8f43fd6633d1', 'index': '1', 'timestamp': '1506172482', 'price': '220', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'ask'}, {'orderId': '7040db5f-0770-43bc-b3bd-aabe1033915f', 'index': '2', 'timestamp': '1506172261', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '7f847e8d-6b90-4c9a-9b0b-293de972dd5d', 'index': '3', 'timestamp': '1506172242', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': 'b6db35c4-8a44-4a21-bcb4-a6a8bfb4aebe', 'index': '4', 'timestamp': '1506172228', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': 'd6e6fd3f-4301-4bcf-8473-bf581ae1901c', 'index': '5', 'timestamp': '1506172214', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '08baf282-d5e2-454d-a884-431b10f4841f', 'index': '6', 'timestamp': '1506172195', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': 'd3163b30-4343-424a-b6ab-0c4a722ca2e4', 'index': '7', 'timestamp': '1506171193', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '6c075c44-529b-4ee2-bc9d-575970e49f80', 'index': '8', 'timestamp': '1506171119', 'price': '180', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'bid'}, {'orderId': '5855587b-44f7-4cf4-bf92-22a84f4dacd9', 'index': '2', 'timestamp': '1506169889', 'price': '210', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'ask'}, {'orderId': '7af5640b-b52f-47ec-a05b-ac0b6ecd680c', 'index': '3', 'timestamp': '1506169646', 'price': '210', 'qty': '1.0000', 'feeRate': '0.001', 'type': 'ask'}]
    # limit_orders('xrp')

    # all_limit_orders()

    # return : ['bch', 'qtum', 'krw', 'etc', 'btc', 'eth', 'xrp']
    # all_currency()

    # return : None
    # cancel('4efa30cd-449c-4bd5-9133-650703a6f453', '100', '1.0000', 0, 'xrp')

    # return : None
    # cancel_all('xrp')

    # return : None
    #cancel_asks('eth')

    # return : None
    #cancel_bids('eth')

    # return : market orders
    market_orders('xrp')

    # return : 219
    #ret = highest_market_bid('xrp')
    #print(ret)

    # return : 220
    #ret = highest_market_ask('xrp')
    #print(ret)



    # return 123400
    price = '440749'
    ret = coineone_krw(price)
    print(ret)

