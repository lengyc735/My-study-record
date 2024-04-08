'''
通用运算符
+  合并  支持类型：字符串 列表 元组
*  复制  支持类型：字符串 列表 元组
in  元素是否存在  支持类型：字符串 列表 元组 字典
not in  元素是否不存在  支持类型：字符串 列表 元组 字典
'''

str1 = 'aa'
str2 = 'bb'

list1 = [2,3]
list2 = [40,50,2]

t1 = (2,3,4)
t2 = (9,0)

dict1 = {'name':'python'}
dict2 = {'age':77}

# 合并
print(str1+str2)
print(list1+list2)
print(t1+t2)

# 复制
print(str1*2)
print(list2*2)
print(t2*2)

# in 和 not in 会返回 False 或 Ture