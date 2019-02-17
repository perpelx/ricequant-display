# -*- coding:utf-8 -*-
from __lib__plot import DisplayCandleStick
import tushare as ts 

def main():
    data = ts.get_hist_data('600848')[0:75]
    cs = DisplayCandleStick(data)
    print(cs.data)
    cs.show_candle_stick(25)

if __name__ == "__main__":
    main()