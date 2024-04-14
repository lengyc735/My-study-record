import numpy as np 

# 创建一维数组
a=np.arange(10)
print(a)
# 索引访问 索引从0开始 长度-1
print('索引0处的元素:',a[0])
print('索引5处的元素:',a[5])

# 负索引 访问 倒数第一个的索引为-1
print('访问最后一个元素:',a[-1])
print('访问倒数第三个元素:',a[-3])

# 切片操作
print(a[:]) #全部元素
print(a[3:]) #从索引3开始到结尾
print(a[3:5]) #3-5
print(a[1:7:2])  #1-7 步长为2