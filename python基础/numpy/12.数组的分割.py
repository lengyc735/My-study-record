import numpy as np

# 创建一维数组
a=np.arange(1,13)
# 调用split函数进行分割
print('传递整数，平均分割')
r=np.split(a,4,axis=0)
print(r)

print('传递数组 按位置分割')
r=np.split(a,[4,6])
print(r)

# 二维数组进行分割
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(a)
print('axis=0 垂直方向 平均分割')
r,w=np.split(a,2,axis=0)
print(r);print(w)

print('axis=0 垂直方向 按位置分割')
r,w,k=np.split(a,[2,3],axis=0)
print(r);print(w);print(k)

print('axis=1 水平分割 平均分割')
r,w=np.split(a,2,axis=1)
print(r);print(w)

print('axis=1 水平分割 按位置分割')
r,w=np.split(a,[3],axis=1)
print(r);print(w)

# 使用hsplit()水平分割
r,w=np.hsplit(a,2)
print(r);print(w)

# 位置分割
r,w=np.hsplit(a,[3])
print(r);print(w)


# 使用vsplit垂直分割
r,w=np.vsplit(a,2)
print(r);print(w)

# 按位置分割
r,w =np.vsplit(a,[3])
print(r);print(w)