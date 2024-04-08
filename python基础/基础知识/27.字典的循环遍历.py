# 1.遍历字典的key
dict1 = {'name':'laowang','age':44,'gender':'男'}

for key in dict1.keys():
    print(key)

# 2.遍历字典的value

for value in dict1.values():
    print(value)

# 3.遍历字典的元素

for item in dict1.items():
    print(item)

# 4.遍历字典的键值对(拆包数据)
for key,value in dict1.items():
    print(f'{key}={value}')
