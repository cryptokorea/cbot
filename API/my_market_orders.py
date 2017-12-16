# Python 2.x

import urllib
import ast
import sys
import my_api

def get_result(currency):
    func_name = get_result.__name__
    try:
        params = urllib.urlencode({'currency': currency})
        content = urllib.urlopen("https://api.coinone.co.kr/orderbook?%s" % params)
        ret = content.read()
        ret2 = ast.literal_eval(ret)
        print("[CHECK][%s][LINE: %s][FUNC : %s]" % (my_api.my_time(), sys._getframe().f_lineno, func_name), ret2)
        return ret2
    except:
        print("[ERR][%s][LINE: %s][FUNC : %s]" % (my_api.my_time(), sys._getframe().f_lineno, func_name))
        return False


if __name__   == "__main__":
    #get_result('xrp')
    print(get_result('xrp'))
    print(get_result('eth'))
    print(get_result('btc'))








