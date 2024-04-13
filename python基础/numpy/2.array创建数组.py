# 导入numpy
import numpy as np
# 使用array函数创建一维数组
a=np.array([1,2,3,4])
print(a)
print(type(a))

# 使用array函数创建二维数组
b=np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print(type(b))

# 使用array函数创建三维数组
c=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(c)
print(type(c))

# array函数ndim使用
e=np.array([7,8,9],dtype=float,ndmin=3)
print(e)