# 所谓修改字符串，指的就是通过函数的形式修改字符串中的数据

"""
1.replace(): 替换
语法：
    字符串序列.replace(旧子串,新子串,替换次数)
注意：替换次数如果查出子串出现次数，则替换次数为该子串出现次数
"""

mystr = 'hellow world and itcast and itheima and python'
# replace() 把and换成he  ** 说明replace函数有返回值，返回值是修改后的字符串
new_str1 = mystr.replace('and','he')
new_str2 = mystr.replace('and','he',1)
# 替换次数如果超出子串出现的次数，表示替换所有该子串
new_str3 = mystr.replace('and','he',7)
print(mystr)
print(new_str1)
print(new_str2)
print(new_str3)
#*** 调用了replace函数后，发现原有字符串的数据并没有做到修改，修改后的数据是replace函数的返回值
#--- 说明 字符串是不可变数据类型
# 数据是否可以划分为 可变类型 和 不可变类型

""""
2.split():分割
语法：
    字符串序列.split(分割字符,num)
注意：num表示的是分割字符出现的次数，即将来返回数据个数为num+1个
"""

# splist()--分割，返回一个列表，会丢失分割字符
list1 = mystr.split('and')
list2 = mystr.split('and',2)
print(list1)
print(list2)

""""
3.join():用一个字符或子串合并字符串，即将多个字符串合并为一个新的字符串
语法:
    字符或子串.join(多字符组成的序列)
"""

# join ()--合并列表里面的字符串数据为一个大字符串
mylist4 = ['aa','bb','cc']

# aa...bb...cc
new_str4 = '...'.join(mylist4)
print(new_str4)