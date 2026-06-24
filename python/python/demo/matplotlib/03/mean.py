"""
demo02_mean.py  均值
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt

def dmy2ymd(dmy):
	dmy = str(dmy)
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t

dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices, volumes= \
	np.loadtxt('./data/da_data/aapl.csv', 
		delimiter=',', usecols=(1,3,4,5,6,7),
		unpack=True, dtype='M8[D],f8,f8,f8,f8,f8',
		converters={1:dmy2ymd})

# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
# 设置刻度定位器
import matplotlib.dates as md
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
# 每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度文本格式
ax.xaxis.set_major_formatter(md.DateFormatter('%Y/%m/%d'))
# 将dates数组中的日期数据转换为matplotlib.dates.datetime类型，以便于后续的日期格式化和绘图操作。
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
	label='Closing Price', linewidth=2,
	linestyle='--')

# 计算收盘价均值
m = np.mean(closing_prices)
m = closing_prices.mean()
mp.hlines(m, dates[0], dates[-1], color='orangered',
	label='Mean(cp)')

# 计算VWAP  成交量加权平均价格
vwap = np.average(closing_prices, weights=volumes)
mp.hlines(vwap, dates[0], dates[-1], 
	color='blue', label='VWAP')

# 模拟计算TWAP  时间加权平均价格
w = np.linspace(1, 7, closing_prices.size)
twap = np.average(closing_prices, weights=w)
mp.hlines(twap, dates[0], dates[-1], 
	color='red', label='TWAP')




mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
