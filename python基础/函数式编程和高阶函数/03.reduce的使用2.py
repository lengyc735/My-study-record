from functools import reduce

# reduce将列表转化为整数
a=[1,2,3,4,5,6,7,8,9]

def fun(x,y):
    return x*10+y

result=reduce(fun,a)
print(result)