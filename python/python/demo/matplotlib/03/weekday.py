'''
weekday.py  星期几的收盘价平均值
'''
import numpy as np
import datetime as dt
def dmy2ymd(dmy):
	dmy = str(dmy)
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	return time.weekday()

dates, opening_prices, highest_prices, \
	lowest_prices, closing_prices, volumes= \
	np.loadtxt('./data/da_data/aapl.csv', 
		delimiter=',', usecols=(1,3,4,5,6,7),
		unpack=True, #将每一列的数据分别赋值给不同的变量，当为false时，返回的是一个数组
		converters={1:dmy2ymd})
 

ave_princes=np.zeros(5)
for i in range(ave_princes.size):
    # 利用掩码，求出每个星期的收盘价平均值
	ave_princes[i]=closing_prices[dates==i].mean()
print(ave_princes)

