import matplotlib.pyplot as mp

mp.figure('Figure AAA', # 创建图表AAA, 窗口标题栏文本
          figsize=(18, 10), # 设置图表大小
          dpi=100, # 设置图表分辨率
          facecolor='lightgray' # 图表背景色
          )
mp.title('Figure AAA title', # 设置图表标题 显示在图表上方
         fontsize=16 # 设置标题字体大小
         )
mp.grid(linestyle=':')

mp.figure('Figure BBB', facecolor='gray')
mp.title('Figure BBB title', fontsize=16)
mp.grid(linestyle='-.')

mp.figure('Figure AAA') # 切换到图表 AAA
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
# mp.tick_params() 用于自定义坐标轴刻度的样式。
mp.tick_params(labelsize=20) # 指定刻度标签的字体大小为 8

mp.tight_layout() # 自动调整图表的布局，避免标签或标题被裁剪。

mp.show()
