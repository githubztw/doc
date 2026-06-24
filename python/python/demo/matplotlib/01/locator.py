"""
demo07_locator.py 刻度定位器
"""
import numpy as np
import matplotlib.pyplot as mp

locators = ['mp.NullLocator()', #不显示任何刻度。
			'mp.MultipleLocator(1)', # 间隔1
			'mp.MaxNLocator(nbins=3)', #最多显示 3 个刻度
			'mp.AutoLocator()']  #由系统自动选择刻度的绘制位置。

mp.figure('Locator', facecolor='lightgray')
mp.title('Locator', fontsize=18)

#遍历 locators 列表中的每个刻度定位器。
for i, locator in enumerate(locators):
    #创建一个4行 1 列的子图网格，并选择第 i+1 个子图。
	mp.subplot(len(locators), 1, i+1)
	ax = mp.gca()
    #设置当前子图的x轴主刻度定位器。
	ax.xaxis.set_major_locator(eval(locator))
    #设置当前子图的x轴的副刻度间隔为 0.1
	ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
	# ax.xaxis.set_minor_locator(mp.NullLocator()) # 不显示副刻度。
    #设置x轴的范围为1到 10。
	mp.xlim(1, 10)
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	ax.spines['left'].set_color('none')
	ax.spines['bottom'].set_position(('data', 0.5))
	mp.yticks([])

mp.show()


