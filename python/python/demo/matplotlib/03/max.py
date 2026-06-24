"""
demo02_mean.py  均值
"""
import numpy as np
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

# 评估30天股价的波动区间
max_val = np.max(highest_prices)
min_val = np.min(lowest_prices)
print(max_val, '~', min_val)

# 获取最高价与最低价的日期
max_ind = np.argmax(highest_prices)
min_ind = np.argmin(lowest_prices)
print('max:', dates[max_ind])
print('min:', dates[min_ind])

# 测试maximum与minimum
a = np.arange(1, 10)
print(a)
b = np.arange(10, 19)
print(b)
print(np.maximum(a, b), '<- maximum()')
print(np.minimum(a, b), '<- minimum()')