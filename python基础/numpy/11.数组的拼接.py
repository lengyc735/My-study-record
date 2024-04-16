import numpy as np

# 创建两个数组
a=np.array([[1,2,3,],[4,5,6]])
b=np.array([[11,12,13],[14,15,16]])
print(a);print(b)

# 使用hstack进行水平拼接
r=np.hstack([a,b])   # r=np.hstack((a,b)) 是一样的
print(r)

# 使用vstack进行垂直方向拼接
v=np.vstack((a,b))
print(v)

# concatenate的使用
print('axis=0 默认情况 垂直方向拼接 相当于vstack')
c1=np.concatenate((a,b),axis=0)
print(c1)

# 二维数组有两个轴 axis=0 axis=1
print('axis=1 水平拼接 相当于hstack')
c2=np.concatenate((a,b),axis=1)
print(c2)

# 三维数组有三个轴 axis=0 1 2
a=np.arange(1,13).reshape(1,2,6)
print(a,a.shape)
b=np.arange(101,113).reshape(1,2,6)
print(b,b.shape)
c3=np.concatenate((a,b),axis=0)
print(c3,c3.shape)
# axis=1 2 3分别对应三个维度相加，写则加不写不加