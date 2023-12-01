'''
字典里面的数据是以'键值对'形式出现，字典数据和数据顺序没有关系，即字典不支持下标
后期无论数据如何变化，只需要按照对应的键的名字查找数据即可
符号为{}  数据为键值对形式  各个键值对用逗号隔开 
'''

# 1.有数据的字典
dict1 = {'name':'xiaoleng','age':18,'gender':'男'}
print(dict1,type(dict1))

# 2.没有数据的字典(空字典)
dict2 = {}
dict3 = dict()
print(dict2,type(dict2))
print(dict3,type(dict3))

# 注意：字典为可变类型