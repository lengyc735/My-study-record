'''
容器类型转换
tuple()  将序列转换为元组
list()   将序列转换为列表
set()    将序列转换为集合
'''

t1 = 'aaabcdef'
print(list(t1))
print(tuple(t1))
print(set(t1))
print(t1,type(t1))
# 此功能可以利用集合去重