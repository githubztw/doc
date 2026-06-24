"""
demo10_bubble.py
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma


# 自定义一种可以存放在 ndarray 里的类型，用于保存一个球
n = 100
balls = np.zeros(n, dtype=[
    ('position', 'f8', 2), # 示每个球的位置由2个float64表示
    ('size', 'f8', 1),
    ('growth', 'f8', 1), # 示每个球的增长速度，由1个float64表示
    ('color', 'f8', 4)]) # 示每个颜色由4个float64表示

# 生成一个形状为 (n, 2) 的二维数组。数组中的每个元素是介于0和 1之间的随机浮点数
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 60, n).reshape(n, 1)  # 修改：确保 size 是 (n,1) 的形状
balls['growth'] = np.random.uniform(10, 20, n).reshape(n, 1)  # 修改：确保 growth 是 (n,1) 的形状
balls['color'] = np.random.uniform(0, 1, (n, 4))
# 画图
mp.figure('Animation', facecolor='lightgray')
mp.title('Animation', fontsize=18)
sc = mp.scatter(balls['position'][:, 0],
               balls['position'][:, 1], s=balls['size'],
               color=balls['color'])


def update(number):
    ind = number % n
    # #每次让一个气泡破裂，随机生成一个新的
    balls[ind]['size'] = np.random.uniform(60, 80, 1)
    balls[ind]['size']=np.random.uniform(40, 70, 1)
    balls[ind]['position']=np.random.uniform(0, 1, (1, 2))
    #不断更新散点大小
    balls['size'] += balls['growth']
    # 更新位置和颜色
    balls['position'] += np.random.normal(0, 0.01, (n, 2))
    balls['color'] = np.random.uniform(0, 1, (n, 4))
    # 修改：将 (n,1) 形状的 size 数组展平为 (n,) 形状
    sc.set_sizes(balls['size'].ravel()) 
    # 更新散点的位置 
    sc.set_offsets(balls['position'])
    # 修改填充颜色
    sc.set_facecolors(balls['color'])


# 执行动画
# mp.gcf():	获取当前窗口
# interval 单位:毫秒
anim = ma.FuncAnimation(
    mp.gcf(), update, interval=100)

mp.show()