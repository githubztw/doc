import numpy as np
import datetime as dt

def dmy2wday(dmy):
	dmy = str(dmy)
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	return time.weekday()

wdays, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        './data/da_data/aapl.csv',
        delimiter=',', usecols=(1, 3, 4, 5, 6),
        unpack=True, converters={1: dmy2wday})
  
# 找到周一的**索引**,返回的是一个数组类型的元组，元组中只有一个元素，所以取[0]
first_mon = np.where(wdays==0)[0][0]

# 找到周五的**索引**
last_fri = np.where(wdays==4)[0][-1]

# 截取周一至周五的所有数据
wdays = wdays[first_mon:last_fri+1]

indices = np.arange(first_mon, last_fri+1)

#把周一至周五每天的indices值统计为5个数组
mon_indices = indices[wdays==0]
tue_indices = indices[wdays==1]
wen_indices = indices[wdays==2]
thu_indices = indices[wdays==3]
fri_indices = indices[wdays==4]

max_len = np.max((mon_indices.size, tue_indices.size, wen_indices.size, thu_indices.size, fri_indices.size))
# pad_width 参数指定了在数组两端填充的宽度。
# 元组的第一个元素 0 表示在数组的前面不进行填充。
# max_len - mon_indices.size表示填充数量的最大长度

mon_indices = np.pad(mon_indices, pad_width=(0, max_len-mon_indices.size), mode='constant', constant_values=-1)
indices = np.vstack((mon_indices,tue_indices,wen_indices,thu_indices,fri_indices))

# numpy将会把每一行的indices传入summary函数执行业务
def summary(indices):
    indices = indices[indices!=-1]
    opening_price = opening_prices[indices[0]]  # 某一天（比如周一）的开盘价
    # highest_prices 是一个包含所有交易日最高价的数组。indices 是一个包含某一天（比如周一）所有交易日索引的数组。
    # 从 highest_prices 数组中提取出周一所有交易日的最高价。
    highest_price = highest_prices[indices].max() # 某一天（比如周一）的最高价
    lowest_price = lowest_prices[indices].min()  # 某一天（比如周一）的最低价
    closing_price = closing_prices[indices[-1]]  # 某一天（比如周一）的收盘
    return opening_price, highest_price, lowest_price, closing_price

r = np.apply_along_axis(summary, 1, indices)

# %g 表示使用通用格式，根据数据的大小自动选择合适的格式。
np.savetxt('./data/da_data/summary.csv', r, delimiter=',', fmt='%g')

