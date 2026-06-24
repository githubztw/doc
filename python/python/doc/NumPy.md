# numpy 

## 1. 集合
**数据类型**
+ str、int、float、、bool、list。
+ complex:数据类型用于表示复数
  `np.array([1 + 2j, 3 - 4j, 5 + 6j], dtype=np.complex)`
+ None: 通常用于表示缺失或未定义的数据
  `none_array = np.array([1, 2, None, 4])`

+ numpy数组

```python
import numpy as np
arry = [1,2,3,4,5]
nu_arry = np.array(arry,dtype=int) # 定义numpy数组
nu_list = nu_arry.tolist() # 转换成集合

print(nu_arry+10) # [11 12 13 14 15]  同理可以做各种运算
print(nu_arry.dtype) # int 检查数据类型

# 二维数组
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print('Shape: ', two_dimension_array.shape) # (3, 3) 检查数组的形状
print('Size:', two_dimension_array.size) # 9  检查数组的元素个数
print('Data type:', two_dimension_array.dtype) # int64

```
+ **切割**
```python
#创建数组[行:列:step] step为步长
two_dimension_array[:,0] # [1 4 7]  第一列
two_dimension_array[:,1] # [2 5 8]  第二列
two_dimension_array[:,2] # [3 6 9]  第三列
two_dimension_array[0:2, 0:2] # [[1 2] [4 5]] # 第一行和第二行的前两个元素

# 三个参数为步长
two_dimension_array[::-1,::-1] # [[9 8 7] [6 5 4] [3 2 1]]  行列发转，倒序
  ```
+ **掩码**
``` python
import numpy as np
a = np.arange(1, 10)
mask = [True, False,True, False,True, False,True, False,True]
print(a[mask]) # 1 3 5 7 9,返回对应为true的元素
```
+ **初始化**
```python
# 初始化
a= np.ones(shape=(3,3),dtype=int,order='C') #  C 行优先,与C语言交互时，效率较高
#[[1 1 1]
# [1 1 1]
# [1 1 1]]
b= np.zeros(shape=(3,3),dtype=int,order='F') # F 列优先
# [[0 0 0]
# [0 0 0]
# [0 0 0]]

#U3 代表最大长度为3的Unicode字符串。在 Python3 中，字符串默认是Unicode字符串
data=[
	('zs', [90, 80, 85], 15),
	('ls', [92, 81, 83], 16),
	('ww', [95, 85, 95], 15)
]

a = np.array(data, dtype='U3, 3int32, int32') 
```
+ **reshape ：** 重新定义数组的形状
```python
first_shape  = np.array([(1,2,3), (4,5,6)])
reshaped = first_shape.reshape(3,2) # [[1 2],[3 4],[5 6]]


first_shape.ravel() # 将数组first_shape为1维数组
n=first_shape.flatten() # 将数组first_shape为1维数组,不改变原有数组
```
+ **random ：** 随机数
```python
random_float = np.random.random() #生成一个float类型随机数
print(type(random_float)) # <class 'float'>

random_floats = np.random.random(5) #生成长度为5的float类型随机数组
print(type(random_floats)) # <class 'numpy.ndarray'>


np.random.randint([min], [max],size=(3,3)]) # 生成3行3列的随机整数,size为生成的数组的形状

# 生成一个长度为80的随机数组，其中每个元素都从均值为79、标准差为15的正态分布（也称为高斯分布）的随机数数组。
np.random.normal(79, 15, 80)
```
+ **arange :** 范围
```python
 np.arange(0, 10, 2) # [0 2 4 6 8] 步长为2
```
+ **重复序列 :** 
```python
# tile 整体重复
np.tile(np.array([1,2,3]), 2) # [1 2 3 1 2 3] # 重复数组‘

#repeat 重复元素
np.repeat(np.array([1,2,3]), 2) # [1 1 2 2 3 3] # 重复元素
```
## 统计学

+ **矩阵**
```python
matrix=np.matrix(np.ones((4,4), dtype=float)) # 创建一个4x4 的矩阵
np.asarray(matrix) # 矩阵成数组
```
