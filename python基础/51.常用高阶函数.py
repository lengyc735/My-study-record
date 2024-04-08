"""
内置高阶函数
map()
reduce()
filter()
"""


'''
map()
map(func,lst),将传入的函数作用到lst的每一个元素上，并将结果作为新的Iterator返回
'''

list1 = [1,2,3,4,5]

def func1(x):
    return x ** 2

result1 = map(func1,list1)

print(result1)      # <map object at 0x000001F5D8A8E1C8>
print(list(result1))   # [1, 4, 9, 16, 25]


'''
reduce(func.lst),其中func必须有两个参数，每次func计算的结果继续和序列的下一个元素做累积计算
注意： reduce()传入的func必须接收两个参数
'''

from functools import reduce

list2 = [1,2,3,4,5]

def func2(a,b):
    return a + b

result2 = reduce(func2,list2)

print(result2)   # 15


'''
filter()
filter(func,lst)
用于过滤序列，过滤掉不符合条件的元素，返回一个filter对象，如果要转换为列表，可以用list()转换
'''

list3 = [1,2,3,4,5,6,7,8,9,10]

def func3(x):
    return x % 2 == 0

result3 = filter(func3,list3)

print(result3)  # <filter object at 0x000001F5D8A8E1C8>
print(list(result3))  # [2, 4, 6, 8, 10]
