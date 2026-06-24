"""
demo12_loadtxt.py  加载文件
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

'''
def dmy2ymd(dmy):
    # 处理可能的bytes或numpy.bytes_类型输入
    if isinstance(dmy, (bytes, np.bytes_)):
        dmy_str = dmy.decode('utf-8')
    else:
        dmy_str = str(dmy)
    # 解析原始日期格式并转换为datetime对象
    time = dt.datetime.strptime(dmy_str, '%d-%m-%Y')
    # 直接返回datetime对象，Numpy会自动转为datetime64[D]
    return time
'''

def dmy2ymd(dmy):
    dmy = str(dmy)
    time = dt.datetime.strptime(dmy, '%d-%m-%Y')
    return time

#\表示换行
dates, opening_prices, highest_prices,lowest_prices, closing_prices = np.loadtxt(
    './data/da_data/aapl.csv', 
	 delimiter=',', usecols=(1,3,4,5,6),
	 unpack=True, dtype='M8[D],f8,f8,f8,f8',
	 converters={1:dmy2ymd} #第2列的数据，将应用 dmy2ymd 函数进行转换。
  ) 


# 绘制收盘价折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.grid(linestyle=':')
# 设置刻度定位器
ax = mp.gca() # 获取当前轴对象
# 将主刻度定位在每周的星期一（Monday）
ax.xaxis.set_major_locator(
	md.WeekdayLocator(byweekday=md.MO)) 
# 每天一个次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置主刻度文本格式
ax.xaxis.set_major_formatter(
	md.DateFormatter('%Y/%m/%d'))
dates = dates.astype(md.datetime.datetime)




# 绘制折线图 x=dates, y=closing_prices
'''
mp.plot(dates, closing_prices, color='dodgerblue',
	label='Closing Price', linewidth=2,
	linestyle='--')
'''


#绘制每一天的蜡烛图
#填充色：涨为白色，跌为绿色
rise = closing_prices >= opening_prices
color = np.array([('white' if x else 'limegreen') for x in rise])
#边框色：涨为红色，跌为绿色
edgecolor = np.array([('red' if x else 'limegreen') for x in rise])

#绘制线条
# bottom 表示起始位置
mp.bar(dates, highest_prices - lowest_prices, 0.1,
	bottom=lowest_prices, color=edgecolor)
#绘制方块
mp.bar(dates, closing_prices - opening_prices, 0.8,
	bottom=opening_prices, color=color, edgecolor=edgecolor)



mp.legend()
#返回当前的图形对象，自动调整 x轴的日期标签，使其更易于阅读。它会旋转日期标签，使其不会重叠，并且会根据图形的大小和布局自动调整标签的位置
mp.gcf().autofmt_xdate()
mp.show()
