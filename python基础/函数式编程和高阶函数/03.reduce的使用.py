from functools import reduce

# 计算序列累加和
a=[1,2,3,4,5,6,7,8,9,10]

# 简单代码实现 
sum=0
for i in a:
    sum+=i
print('累加和：',sum)

# reduce实现
def sumTest(x,y):
    return x+y
sum2=reduce(sumTest,a)
print('累加和2:',sum2)