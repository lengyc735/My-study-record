'''
1.del
del 目标   或   del(目标)
del 可以删除指定下标的数据
'''

list_1 = ['a','c','b']
del list_1
# print(list_1)   打印不出来

list_2 = ['a','c','e']
del list_2[0]
print(list_2)

"""
2. pop()删除指定下标的数据，如果不指定下标，默认删除最后一个下标的数据，
无论按下标删除还是删除最后一个数据，poo都会返回被删除的这个数据
语法： 列表序列.pop(下标)
"""
a = list_2.pop()
print(a)
print(list_2)

# 3.remove(要删除的数据)
list_3 = ['wudi',12,'就']
list_3.remove("就")
print(list_3)

# 4.clear()---清空列表
list_4 = [',',1]
list_4.clear()
print(list_4)