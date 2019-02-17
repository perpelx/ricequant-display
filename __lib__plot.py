# -*- coding:utf-8 -*-
import talib as ta
import pandas as pd
import numpy as np
from functools import wraps
import time
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
import mpl_finance as mpf

# 装饰器，计算消耗时间
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print("Total time running %s: %s seconds" % (function.__name__, str(t1 - t0)))
        return result

    return function_timer

class DisplayCandleStick:
    """
    显示蜡烛图
    """
    def __init__(self, data):

        # 初始化数据
        self.data = data[0:60]
        self.max_price = self.data['high'].max()
        self.min_price = self.data['low'].min()
        self.max_vol = self.data['volume'].max()
        self.min_vol = self.data['volume'].min()
        self.data.index = pd.to_datetime(self.data.index)
        self.sma_10 = ta.SMA(np.array(self.data['close']), 10)
        self.sma_30 = ta.SMA(np.array(self.data['close']), 30)

    def show_candle_stick(self):

        # 创建图像和子图
        fig = plt.figure(figsize=(20, 13))
        ax = fig.add_axes([0.015,0.4,1,0.6])
        ax2 = fig.add_axes([0.015,0.05,1,0.35])

        # k 线
        mpf.candlestick2_ochl(ax, 
                self.data['open'], self.data['close'], self.data['high'],self.data['low'], 
                width=0.5, colorup='r', colordown='g', alpha=0.8)

        # 设置横纵轴坐标
        # ax.set_xticks(range(0, len(self.data.index), 10))
        ax.set_yticks(range(int(self.min_price*0.9),int(self.max_price*1.1),2))
        ax.set_ylabel('price')
        ax2.set_yticks(range(0,int(self.max_vol*1.1),50000))
        ax2.set_ylabel('vol')
        ax.plot(self.sma_10, label='10 日均线')
        ax.plot(self.sma_30, label='30 日均线')

        # 创建图例
        ax.legend(loc = 'upper center') 

        # 网格
        ax.grid(True)

        # 成交量
        mpf.volume_overlay(ax2, self.data['open'], self.data['close'], self.data['volume'], 
                           colorup='r', colordown='g', width=0.5, alpha=0.8)
        # ax2.set_xticks(range(0, len(self.data.index), 10))
        ax2.set_xticklabels(self.data.index.strftime('%Y-%m-%d')[::10], rotation=30)
        ax2.grid(True)
        plt.show()