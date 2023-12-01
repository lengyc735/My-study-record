# tuple 是不可变数据

t1 = (1,7,5)
print(type(t1))

t2 = (7,)   # 注意 逗号 必须加，不然不是元组
print(type(t2))

t3 = (7)
print(type(t3))     #输出结果为int

# 如果单个数据不加逗号，会返回原本的类型

'''
元组数据不支持修改，只支持查找
index()  查找数据
couunt()  统计数据出现次数
len()  统计数据个数
'''
t4 = ('11','aa','BB','无敌')
print(t4[1])

print(t4.index('BB'))

print(t4.count('无敌'))

print(len(t4))

# 元组本身是不能修改的，但是可以套列表，对列表进行修改，从而修改元组数据

t1 = (111,'111',['234','aaa'])
t1[2][1] = 456
print(t1)
