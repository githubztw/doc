"""
demo04_subplot.py  子图
"""
import numpy as np
import matplotlib.pyplot as mp

mp.figure('Subplot', facecolor='lightgray')
for i in range(1, 10):
	mp.subplot(3,3,i)
	mp.text(
     0.5, 0.5, # 文本的坐标位置，(0.5, 0.5) 表示子图的中心。
     i, # 文本内容
     size=36, 
     ha='center', # 水平对齐方式
     va='center', # 垂直对齐方式
     alpha=0.6 # 文本的透明度为 0.6
   )
    #隐藏当前子图的 x 轴和 y 轴刻度。
	mp.xticks([])
	mp.yticks([])
	mp.tight_layout()
mp.show()