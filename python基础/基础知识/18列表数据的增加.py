# 列表增加数据
"""
append():列表（结尾）追加数据
列表序列.append(数据)
"""
name_list = ['leng','Tom','Rose']

name_list.append('xaioming')    # 加个列表之类的也可以
print(name_list) 


"""
extend():列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
列表数据.extend(数据)
"""
name_list2 = ['1','2','3']
name_list2.extend('daming')
print(name_list2)

list = ['1','2','7']
list.extend(['我无敌','who\'re you'])
print(list)

"""
insert():指定位置追加数据
列表序列.insert(位置下标,数据)
"""
list_1 = ['wo','ni','ta']
list_1.insert(1,'women')
print(list_1)