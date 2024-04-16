import numpy as np

a=np.arange(9).reshape(3,3)
b=np.array([10,10,10])
print('加法')
print(np.add(a,b))
print(a+b)
print('减法')
print(np.subtract(b,a))
print(b-a)

# out参数的使用
y=np.empty((3,3))
np.multiply(a,10,out=y)
print(y)

# 三角函数
a=np.array([0,30,60,90])
print(np.sin(a))

# 取整around  ceil  foor
a=np.array([1.0, 4.55, 113, 0.567, 25.532])
print('around:',np.around(a))    # 四舍五入
print('ceil:',np.ceil(a))        # 向上取整
print('floor',np.floor(a))       # 向下取整


# 统计函数
# power()
a=np.arange(1,13).reshape(3,4)
print('原数组:')
print(a)
print('power:',np.power(a,2))

# power中out的使用
x=np.arange(5)
y=np.zeros(10)
np.power(2,x,out=y[:5])
print(y)


# median()
# 一维数组的中位数
a=np.array([4,3,2,5,2,1])
print(np.median(a))

# 二维数组 要通过axis指定轴
a=np.arange(1,13).reshape(3,4)
print(a)
print('垂直方向',np.median(a,axis=0))
print('水平方向',np.median(a,axis=1))


# mean求平均值
# 一维数组
a=np.array([4,3,2,5,2])
print(np.mean(a))
#二维数组 axis指定轴求平均
a=np.arange(1,13).reshape(3,4)
print(a)
print('axis=0 垂直方向',np.mean(a,axis=0))
print('axis=1 水平方向',np.mean(a,axis=1))

# sum()  max()  min()
a=np.array([4,3,2,5,2])
print('max:',np.max(a))
print('sum:',np.sum(a))
print('min:',np.min(a))

# argmax argmin 最大值和最小值的下标
print('argmax:',np.argmax(a))
print('argmin:',np.argmin(a))