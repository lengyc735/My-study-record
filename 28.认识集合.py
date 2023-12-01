# 创建集合使用{}或set(),但是如果要创建空集合只能使用set(),因为{}用来创建字典

s1 = {10,20,30,40,50}
print(s1)
# 集合没有顺序，不支持下标

s2 = {10,10,20,20,30,40}
print(s2)
# 集合可以去重

s3 = set('abcdefg')
print(s3)
# set()也可以创建集合

s4 = set()
print(s4)
print(type(s4))
# 空集合只能用set()创建

s5 = {}
print(s5)
print(type(s5))
# 用{}创建的是一个空字典