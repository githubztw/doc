"""
demo08_gridline.py  刻度网格线
"""
import matplotlib.pyplot as mp
y = [1, 10, 100, 1000, 100, 10, 1]
# 设置刻度定位器
mp.figure('Grid Line', facecolor='lightgray')
#表示2行1的子图网格，第 1 个子图。
mp.subplot(211)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
# 刻度网格线
# which='major'表示主刻度，'minor'表示副刻度。
# axis='both'表示刻度网格线在 x 轴和 y 轴上。
ax.grid(which='major', axis='both',
		color='orangered', linewidth=0.5)
ax.grid(which='minor', axis='both', 
		color='orangered', linewidth=0.25)
# 绘制折线图，数据点为圆圈，线条为实线。
# 在普通坐标系中绘制曲线
mp.plot(y, 'o-')


##表示2行1的子图网格，第2个子图。
mp.subplot(212)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
# 刻度网格线
ax.grid(which='major', axis='both', 
		color='orangered', linewidth=0.5)
ax.grid(which='minor', axis='both', 
		color='orangered', linewidth=0.25)
# 绘制折线图，数据点为圆圈，，线条为实线。
# 在半对数坐标系中绘制曲线（y 轴是对数刻度，x 轴是线性刻度）。
mp.semilogy(y, 'o-')
mp.show()
