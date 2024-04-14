# 导入numpy
import numpy as np

# range的使用  range(start,end,step)--[start,end)
a=list(range(1,10))
print(a)
b=list(range(10))
print(b)
c=list(range(1,10,3))
print(c)

# arange创建数组
# 使用arange创建1,10的数组
e=np.arange(1,11)
print(e)

# 设置step
f=np.arange(1,11,2)
print(f)

# 设置dtype
g=np.arange(10,20,2,dtype=float)
print(g)