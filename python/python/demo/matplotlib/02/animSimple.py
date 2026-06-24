"""
demo09_anim.py  动画
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

def update(number):
	print(number)

mp.figure("A")
# FuncAnimation 会自动为update函数提供一个参数number，表示当前帧数的序号，该参数是从 0 开始递增的整数，默认情况下每次调用增加 1。
a=ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()