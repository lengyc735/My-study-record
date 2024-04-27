# 一个函数f(x)=x^2,要把这个函数作业在一个列表上

a=[1,2,3,4,5,6,7]

def f(x):
    return x*x

# 编写函数实现
result_list=[]
for i in a:
    result_list.append(f(i))
print(result_list)

# map()实现
it=map(f,a)  # 返回的it是一个可迭代的对象
# print(it)
# 判断是否是可迭代的对象
from collections.abc import Iterator
print('判断是否是可迭代的对象:',isinstance(it,Iterator))
print(list(it))