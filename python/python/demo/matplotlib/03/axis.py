"""
demo06_axis.py  数组的轴向汇总
"""
import numpy as np
#               语文 数学 英语
data = np.array([[80, 81, 92], 
				 [71, 81, 82], 
				 [92, 61, 22], 
				 [83, 73, 42], 
				 [74, 85, 52], 
				 [95, 89, 62], 
				 [96, 91, 72]])

# 轴向汇总

def func(data):
	return data.max(), data.argmax()

r = np.apply_along_axis(func, 1, data)
print(r)
print('-' * 45)


# 按行汇总数据  求均值
avg_scores = []
for i in range(len(data)):
	avg_scores.append(np.mean(data[i]))
print(np.round(avg_scores, 2))

# 按列汇总数据  求最大值
max_scores = []
# shape[1]表示数组的列数
for j in range(data.shape[1]):
	max_scores.append(data[:, j].max())
 
# 保留两位小数
print(np.round(max_scores, 2))