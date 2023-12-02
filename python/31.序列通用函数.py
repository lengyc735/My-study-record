'''
通用函数
len()  计算容器中元素个数
del 或 del()    删除
max() 取最大 
min() 取最小
range(start,end,step)  生成从start到end的数字，步长为step，供for循环使用
enumerate()  用于可遍历对象组合为一个索引序列，同时列出数据和数据下标，一般用于for循环
'''

str1 = 'abcdefg'
list1 = [10,20,30,40,50]
t1 = (20,30,40,50,60)
s1 = {30,40,50,60,70}
dict1 = {'name':'kobe','profession':'raper'}

# len()
print(len(s1))
print(len(dict1)) # len(集合) 为键值对数量

# del()
del(list1[2])
print(list1)

# raange()生成的序列不包含end数字
for i in range (1,12,3):
    print(i)
# 没写开始默认为0，没写步长默认为1,结束不能省略

'''
enumerate()
语法： enumerate(可遍历对象,start=0)
注意：start参数用来设置遍历参数的下标的起始值，默认值为0
'''

list2 = [1,7,89,0]
for i in enumerate(list2):
    print(i)
# enmurate()返回结果是元组，元组第一个数据是原迭代对象的数据对应的下标，元组第二个数据是原迭代对象的数据