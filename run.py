# from multiprocessing import Process
import sys
sys.path.append("C:/Users/user/PycharmProjects/coinone/API")
import my_algo_1
import time
import multiprocessing

def xrp_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "xrp"
    my_algo_1.TRADE_INFO['quantity'] = "10"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "230"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

def eth_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "eth"
    my_algo_1.TRADE_INFO['quantity'] = "0.01"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "340000"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

def etc_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "etc"
    my_algo_1.TRADE_INFO['quantity'] = "0.2"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "16000"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

def qtum_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "qtum"
    my_algo_1.TRADE_INFO['quantity'] = "0.2"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "12000"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

def bch_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "bch"
    my_algo_1.TRADE_INFO['quantity'] = "0.01"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "500000"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

def btc_start(process_name):
    print ("%s thread start!! " % process_name)
    my_algo_1.TRADE_INFO['currency'] = "btc"
    my_algo_1.TRADE_INFO['quantity'] = "0.001"
    my_algo_1.TRADE_INFO['down_percentage'] = "0.95"
    my_algo_1.TRADE_INFO['up_percentage'] = "1.025"
    my_algo_1.TRADE_INFO['limit_bid_price'] = "4800000"
    my_algo_1.main_loop(my_algo_1.TRADE_INFO)

# Define a function for the thread
def print_time(process_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s" % (process_name, time.ctime(time.time()))

if __name__ == '__main__':
    try:
        p = multiprocessing.Process(target=bch_start, args=('bch bot',))
        p.start()
        p2 = multiprocessing.Process(target=etc_start, args=('etc bot',))
        p2.start()
        p3 = multiprocessing.Process(target=eth_start, args=('eth bot',))
        p3.start()
        p4 = multiprocessing.Process(target=xrp_start, args=('xrp bot',))
        p4.start()
        p5 = multiprocessing.Process(target=qtum_start, args=('qtum bot',))
        p5.start()
        p6 = multiprocessing.Process(target=btc_start, args=('btc bot',))
        p6.start()

        p.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()

    except:
        print "Error: unable to start"

    while 1:
        pass
