__author__ = 'Charlie Kim'
import my_api
import time
import datetime
import sys

TRADE_INFO = {
    "currency": 'none',
    "quantity": 'none',
    "down_percentage": 'none',
    "up_percentage": 'none',
    "limit_bid_price": 'none'
}


def price_update(my_list, cur_price, trade_info):
    currency = trade_info['currency']
    func_name = price_update.__name__
    print("[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
    try:
        my_list_len = len(my_list)
        if my_list_len > 60 and my_list_len != 0:
            print("[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
            my_list.pop()
        else:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
        my_list.insert(0, cur_price)
        print(
            "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
    except:
        ts = time.time()
        ts2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print('[ERR][%s][%s]' % (ts2, func_name))


def get_ave(my_list, cur_price, trade_info):
    currency = trade_info['currency']
    func_name = get_ave.__name__
    print("[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
    try:
        price_update(my_list, cur_price, trade_info)
        my_list_len = len(my_list)
        if my_list_len < 50:
            print("[%s][CHECK - YES WAIT for an hour][%s][LINE: %s][FUNC : %s]  my_list_len : %d  " % (
                currency, my_api.my_time(), sys._getframe().f_lineno, func_name, my_list_len))
            return False
        total_count = 0
        for i in range(my_list_len):
            total_count += float(my_list[i])
        print("[%s][CHECK][%s][LINE: %s][FUNC : %s]   total_count / my_list_len : %d" % (
            currency, my_api.my_time(), sys._getframe().f_lineno, func_name, total_count / my_list_len))
        return str(total_count / my_list_len)
    except:
        ts = time.time()
        ts2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print('[%s][ERR][%s][%s]' % (currency, ts2, func_name))
        return False


def my_algo_1_buy(my_list, cur_price, trade_info):
    currency = trade_info['currency']
    down_percentage = trade_info['down_percentage']
    quantity = trade_info['quantity']
    func_name = my_algo_1_buy.__name__
    ave_price = get_ave(my_list, cur_price, trade_info)
    if ave_price == False or cur_price == False:
        print("[%s][CHECK - MAY NEED TIME to CAL][%s][LINE: %s][FUNC : %s]" % (
            currency, my_api.my_time(), sys._getframe().f_lineno, func_name), ave_price, cur_price)
        return False
    print("[%s][CHECK][%s][LINE: %s][FUNC : %s] ave_price of 1 hour : %f  " % (
        currency, my_api.my_time(), sys._getframe().f_lineno, func_name, float(ave_price)))
    try:
        if float(ave_price) < 0.0:
            print(
                "[%s][ERR][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
            return False
        # BUY
        want_buy_price_t = float(ave_price) * float(down_percentage)
        want_buy_price = str(want_buy_price_t)
        print("[%s][CHECK][%s][LINE: %s][FUNC : %s]   want_buy_price : %s" % (
            currency, my_api.my_time(), sys._getframe().f_lineno, func_name, want_buy_price))
        if float(cur_price) <= want_buy_price_t:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s] ave_price of 1 hour : %s, want_buy_price : %s, BUY price : %s, QUANTITY : %s, currency : %s" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name, ave_price, want_buy_price, cur_price,
                    quantity, currency))
            my_api.buy(my_api.coinone_krw(cur_price), quantity, currency)
            return True
        else:
            print(
                "[WAIT][%s][LINE: %s][FUNC : %s] ave_price of 1 hour : %s, want_buy_price : %s, BUY price : %s, QUANTITY : %s, currency : %s" % (
                    my_api.my_time(), sys._getframe().f_lineno, func_name, ave_price, want_buy_price, cur_price,
                    quantity,
                    currency))
            return False
    except:
        print(
            "[%s][ERR][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
        return False


def my_algo_1_sell(cur_price, trade_info):
    currency = trade_info['currency']
    up_percentage = trade_info['up_percentage']
    func_name = my_algo_1_sell.__name__
    print("[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
    sell_price_t = int(float(cur_price) * float(up_percentage))
    sell_price = str(sell_price_t)
    for i in range(3):
        time.sleep(15)
        ret = my_api.balance(currency)
        print(ret)
        qty = ret['avail']
        print(qty)
        print("[%s][CHECK][%s][LINE: %s][FUNC : %s]  cur_price : %s, sell_price : %s, quantity : %s, actual quantity to sell : %s" % (
            currency, my_api.my_time(), sys._getframe().f_lineno, func_name, cur_price, sell_price, qty, my_api.coinone_qty(qty)))
        try:
            if float(qty) > 0.00000000:
                print("[%s][CHECK][%s][LINE: %s][FUNC : %s]  cur_price : %s, sell_price : %s, quantity : %s" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name, cur_price, sell_price, qty))
                my_api.sell(my_api.coinone_krw(sell_price), my_api.coinone_qty(qty), currency)
            else:
                print("[%s][CHECK][%s][LINE: %s][FUNC : %s]  NO QUANTITY TO SELL, try(%d)  " % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name, i))
        except:
            print(
                "[%s][ERR][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))


"""    
    currency = trade_info['currency']
    quantity = trade_info['quantity']
    down_percentage = trade_info['down_percentage']
    up_percentage = trade_info['up_percentage']
    limit_bid_price = trade_info['limit_bid_price']
"""


def main_loop(trade_info):
    currency = trade_info['currency']
    limit_bid_price = trade_info['limit_bid_price']
    func_name = main_loop.__name__
    new = old = time.time()
    my_price_list = []

    while True:
        # SLEEP 60 sec
        diff = 60 - int(new - old)
        # print("DIFF", float(diff))
        if 0 < diff <= 60:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
            time.sleep(diff)
        old = time.time()

        # GET CUR PRICE
        # cur_price = my_api.highest_market_bid(currency)   # buy highest bid price
        cur_price = my_api.highest_market_ask(currency)  # buy lowest ask price
        if int(cur_price) < 0:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
            new = time.time()
            continue
        else:
            print("[%s][CHECK][%s][LINE: %s][FUNC : %s]  cur_price : %s   " % (
                currency, my_api.my_time(), sys._getframe().f_lineno, func_name, cur_price))

        # LIMIT BID
        if int(cur_price) > limit_bid_price:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))
            new = time.time()
            continue
        else:
            print(
                "[%s][CHECK][%s][LINE: %s][FUNC : %s]" % (
                    currency, my_api.my_time(), sys._getframe().f_lineno, func_name))

        # CANCEL ALL BIDS
        my_api.cancel_bids(currency)

        # BUY
        ret = my_algo_1_buy(my_price_list, cur_price, trade_info)
        if ret:
            # SELL
            my_algo_1_sell(cur_price, trade_info)
        new = time.time()


#######################################################################
# MAIN


if __name__ == "__main__":
    TRADE_INFO_TEST = {
        "currency": 'xrp',
        "quantity": '1',
        "down_percentage": '0.95',
        "up_percentage": '1.025',
        "limit_bid_price": '220'
    }
    main_loop(TRADE_INFO_TEST)
