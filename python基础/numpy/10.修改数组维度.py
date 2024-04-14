import numpy as np

#  通过reshape将一维数组修改为二三维
# 创建一个一维数组
a=np.arange(1,25)
print(a)
# 将一维修改为二维
b=a.reshape((3,8))
print(b)

# 将一维修改为三维
c=a.reshape((2,3,4))
print(c)

# 通过np.reshape()进行修改
#bb=np.reshape(a,(3,8)) # 修改为2维
bb=np.reshape(a,(4,3,2))
print(bb)


# 将多维数组修改为一维数组
# a=bb.reshape(24)
a=bb.reshape(-1)
print(a)
# 通过ravel,flatten将多维数组转化为一维数组
# ravel
a=bb.ravel()
print(a)

# flatten
a=bb.flatten()
print(a)