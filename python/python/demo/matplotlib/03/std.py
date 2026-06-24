"""
demo05_std.py  标准差
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
# 总体标准差
std = np.std(closing_prices)
std = closing_prices.std()
print(std)

m = np.mean(closing_prices)
d = closing_prices - m
var = np.mean(d**2)
std = np.sqrt(var)
print(std)
# 样本标准差
std = np.std(closing_prices, ddof=1)
print(std)