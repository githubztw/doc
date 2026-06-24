"""
demo09_scatter.py 散点图
"""
import numpy as np
import matplotlib.pyplot as mp
n = 200
# 生成正态分布随机数
x = np.random.normal(175, 7, n) # 均值/期望值175，标准差7，样本数n
y = np.random.normal(65, 10, n) # 均值/期望值65，标准差7，样本数n
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=18)
mp.grid(linestyle=':')
# d 是每个数据点到中心点的平方距离。
# d 的值越大，越偏离中心位置，颜色越偏向彩虹色系的一端。
d = (x-175)**2 + (y-65)**2
mp.scatter(x, y, marker='o', s=70,
	c=d, cmap='gist_rainbow', #  cmap用于指定颜色映射表
 label='Samples')
mp.legend()
mp.show()
