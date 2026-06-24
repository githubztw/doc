"""
demo03_pie.py   饼状图
"""
import matplotlib.pyplot as mp

#整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.01, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']

mp.figure('Pie', facecolor='lightgray')
# 设置坐标轴的缩放比例为相等。
mp.axis('equal') 
mp.title('Pie', fontsize=18)
mp.pie(values, spaces, labels, colors,
	'%.1f%%', startangle=0, shadow=False)
mp.legend()
mp.show()
