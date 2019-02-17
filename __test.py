# -*- coding:utf-8 -*-
from __lib__plot import DisplayCandleStick
import tushare as ts 

def main():
    data = ts.get_hist_data('600848')[:200]
    print (data)
    cs = DisplayCandleStick(data)
    cs.show_candle_stick()

if __name__ == "__main__":
    main()