'''
return作用：
1.负责函数返回值
2.退出当前函数，导致return下方的所有代码(函数体内部)不执行
'''

def buy():
    return '可乐'

goods = buy()
print(goods)

# 举例：计算任意两个数字的加法，并返回结果

def sum_num(a,b):
    return a + b

result = sum_num(7,5)
print(result)