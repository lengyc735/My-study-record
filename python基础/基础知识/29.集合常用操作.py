'''
集合常用操作————增加
add()  增加单一数据
update()  追加的数据是序列
'''

# add()
s1 = {10,20}
s1.add(100)
print(s1)

s1.add(20)
print(s1)
# 因为集合会去重，add()追加一个重复的，不会进行任何操作
# add()追加序列会报错

# update

s2 = {2,3,4,5}
s2.update([1,2,3,7,0])
print(s2)
# update()追加单个数据会报错

'''
集合常用操作————山粗
remove()  删除集合中的指定数据，如果数据不存在则报错
discard()  删除集合中指定数据，如果数据不存在也不会报错
pop()   随机删除集合中的某个元素，并返回这个数据
'''

s3 = {1,2,3,4,5,6}

# remove()
s3.remove(2)
print(s3)

# discard()
s3.discard(5)
print(s3)
s3.discard(7)
print(s3)

# pop()
a = s3.pop()
print(a)
print(s3)

'''
集合常用操作————查找
in： 判断数据在集合序列
not in：判断数据不在集合序列
'''

s4 = {2,3,4,5,6,7,8,9}
print(10 in s4)  # False
print(2 in s4)   # Ture
print(10 not in s4)  # Ture
print(2 not in s4)   # False
