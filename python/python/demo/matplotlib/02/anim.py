import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

mp.figure("Signal", facecolor='lightgray')
mp.title("Signal", fontsize=14)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]
pl.set_data([],[])

x = 0

def update(data):
	t, v = data
	x, y = pl.get_data()
	x.append(t)
	y.append(v)
	#重新设置数据源
	pl.set_data(x, y)
	#移动坐标轴
	if(x[-1]>10):
        # x[-1]表示最后一个元素值
		mp.xlim(x[-1]-10, x[-1])
# 每隔10毫秒将会先调用生成器，获取生成器返回的数据，
# 把生成器返回的数据交给并且调用update函数，执行更新图像函数
def y_generator():
	global x
	y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
	yield (x, y)
	x += 0.05

anim = ma.FuncAnimation(mp.gcf(), update, y_generator, interval=20)
mp.tight_layout()
mp.show()
