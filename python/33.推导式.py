"""
推导式
分为：列表推导式 字典推导式 集合推导式
"""

'''
列表推导式
作用：用一个表达式创建一个有规律的列表或控制一个有规律列表
列表推导式又叫列表生成式
'''
# 创建一个0到10的列表
list1 = [i for i in range(11)]
print(list1) 

# 创建一个0到10的偶数序列
list2 = [i for i in range(0,11,2)]
print(list2)

list3 = [i for i in range(11) if i % 2 == 0]
print(list3)
# 注意带if的生成式在后面只能加一个if

# 多个for实现生成式
list4 = [(i,j) for i in range(1,3) for j in range(3)]
print(list4)
# 其原理类似for循环嵌套

# if...lse
list5 = [i if i % 2 == 0 else i ** 2 for i in range(11)]
print(list5)
# 注意这样写必须写else

'''
字典推导式
变量 = {key: value for循环}
'''

# 1.创建一个字典，key为1——5，value为这个数字的平方
dict1 = {i: i**2 for i in range(1,6)}
print(dict1)

# 2.将两个列表合并为一个字典
li1 = ['name','age','gender']
li2 = ['kobe',44,'nv']
dict2 = {li1[i]: li2[i] for i in range(len(li1))}
print(dict2)
# 两个列表长度不一样应该取短的，不然会报错

# 3.提取字典中的目标数据
counts = {'MBP':267,'HP':120,'DELL':201,'lenovo':199,'caer':99}
# 需求 提取上述电脑数量中大于200的字典数据
count1 = {key: value for key,value in counts.items() if value >= 200}
print(count1)

'''
集合推导式
用的少，可以去重
'''

list6 = [1,1,2]
set1 = {i**2 for i in list6}
print(set1)