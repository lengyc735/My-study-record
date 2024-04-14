import numpy as np

# 创建一维数组
a=np.arange(1,13)
print(a)
# 对一维数组进行修改形状
a=a.reshape((4,3))
print(a)
# 索引的使用
# 获取第三行
print(a[2])
# 获取第二行 第三列
print(a[1][2])

#  切片的使用
# [行进行行切片，列进行列切片]  [start:stop:step,start:stop:step]
# 获取所有行所有列
print(a[:,:])
# 获取所有行部分列 所有行第二列
print(a[:,1])
# 所有行1，2列
print(a[:,0:2])

# 获取1,2行 3,4列
print(a[:1,2:3])
# 奇数列所有行
print(a[::2,:])
# 2，3行奇数列
print(a[1:2,::2])

#----------------
# 坐标获取 [行,列]
# 获取2行3列的元素
print(a[1][2])
print(a[1,2])

# 获取第二行第三列，第三行第一列
print(a[1,2],a[2][0])
print(np.array([a[1,2],a[2][0]]))
# 使用坐标
print(a[(1,2),(2,0)])

# 负索引使用
print('最后一行')
print(a[-1])
print('行倒序')
print(a[::-1])
print('行列倒序')
print(a[::-1,::-1])