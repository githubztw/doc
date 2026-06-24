"""
demo08_boll.py  布林带
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
	lowest_prices, closing_prices = \
	np.loadtxt('./data/da_data/aapl.csv', 
		delimiter=',', usecols=(1,3,4,5,6),
		unpack=True, dtype='M8[D],f8,f8,f8,f8',
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
ax.xaxis.set_major_locator( # 每周一为主刻度
	md.WeekdayLocator(byweekday=md.MO))
# 每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度文本格式
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
	label='Closing Price', linewidth=2,
	linestyle='--', alpha=0.6)

# 基于时间加权卷积 实现5日均线
kernel = np.exp(np.linspace(-1, 0, 5))
kernel = kernel[::-1] / kernel.sum()
ma53 = np.convolve(closing_prices, kernel, 'valid')
mp.plot(dates[4:], ma53, color='red',
	label='MA53', linewidth=2)
# 绘制上轨与下轨
std53 = np.zeros(ma53.size)
for i in range(std53.size):
	std53[i] = closing_prices[i:i+5].std()
upper = ma53 + 2*std53
lower = ma53 - 2*std53
mp.plot(dates[4:], upper, color='orangered',
	label='upper', linewidth=2)
mp.plot(dates[4:], lower, color='orangered',
	label='lower', linewidth=2)
mp.fill_between(dates[4:], upper, lower,
	upper > lower, color='orangered', alpha=0.2)


mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
