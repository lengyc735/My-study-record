
'''
字典常用操作————增
写法：字典序列[key] = 值
注意：如果key存在则修改这个key对应的值，不存在则新增此键值对 
 '''
dict1 = {'name':'leng','age':18,'gender':'男'}

dict1['id'] = 119
print(dict1)

dict1['name'] = 'lengtiandi'
print(dict1)

'''
字典常用操作————删
del()/del: 删除字典或字典指定键值对
clear(): 清空字典
'''
d1 = {'name':'daming'}
del(d1)
# print(d1)  报错

d2 = {'name':'xiaoming','age':19,'gender':'男'}
del d2['age']  # 若输入不存在是key会报错
print(d2)

d3 = {'age':101}
d3.clear()
print(d3)

"""
字典常用操作————改
写法：字典序列[key] = 值
注意：如果key存在则修改这个key对应的值，如果不存在则新增此键值对
"""
d4 = {'name':'cuihua'}
d4['name'] = 'tiantian'
print(d4)

'''
字典常用操作————查
key值查找
函数查找
'''

d5 = {'name':'daixao','age':120,'gender':'女'}
print(d5['name'])
# 注意输入的key若不存在，会报错

'''
get()
keys()
values()
items()
'''

'''
1.get()
字典序列.get(key,默认值)
注意：如果当前查找的key不存在则返回第二个参数(默认值)，如果省略第二个参数则返回None
'''
d6 = {'name':'aa','age':777,'id':789}
print(d6.get('name'))
print(d6.get('gender','weizhi'))
print(d6.get('gender'))

# 2.keys()   查找字典中所以的key，返回可迭代对象
print(d6.keys())

# 3.values()   查找字典中所有的value,返回可迭代对象
print(d6.values())

# 4.items    查找字典中所有的键值对，返回可迭代对象，里面的数据是元组，元组的数据1，2分别为key,key对应的值
print(d6.items())
