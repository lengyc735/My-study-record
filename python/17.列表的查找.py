# 列表的查找

# 通过下标查找
name_list = ['Tom','Lily','Rose']
print(name_list[0])
print(name_list[1])
print(name_list[2])

# 函数查找
"""
index():返回指定数据所在位置的下标
列表序列.index(数据,开始下标位置,结束下标位置)
注：如果查找的数据不存在会报错
"""
print(name_list.index('Tom'))

#  count():统计指定数据在当前列表出现的次数
print(name_list.count('Lily'))
print(name_list.count('leng'))     # 该数据不存在 不会报错，会返回0

# Len():访问列表长度，即列表中的数据个数
print(len(name_list))            # len()是通用的 

"""
判断是否存在
有两种方法 in  和  not in
in:判断指定数据在某个列表序列，如果在返回Ture,否则返回False
not in:判断某个数据不在列表序列，如果不在返回Ture,否则返回False
"""
print('Rose' in name_list)
print('Rose' not in name_list)

# 注册邮箱，判断邮箱是否存在
name = input('请输入你的邮箱用户名:')
if name in name_list:
    print(f'{name}已经存在，请换一个')
if name not in name_list:
    print(f'用户名{name}不存在，可以注册')