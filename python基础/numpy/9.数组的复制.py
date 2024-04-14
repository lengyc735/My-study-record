import numpy as np

# 创建一个二维数组
a=np.arange(1,13).reshape((3,4))
print(a)
# 对a切片
sub_a=a[:2,:2]
print(sub_a)
# 对sub_a修改
sub_a[0][0]=100
print(sub_a)
print(a)
#  修改sub_a的值a也会被修改

# 复制
sub_aa=np.copy(a[:2,:2]) # 深拷贝
sub_aa[0,0]=200
print(sub_aa)
print(a)
# 复制后修改，不会影响原来的值