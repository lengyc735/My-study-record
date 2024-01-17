# 值都是靠引用来的
# 用id()来判断两个变量是否为同一个值的引用

#  int类型
a = 1
b = a

print(b)

print(id(a))
print(id(b))

a = 2
print(b)
print(id(a))  # 此时得到的是2的内存地址
print(id(b))

# 列表
aa = [10, 20]
bb = aa

print(id(aa))
print(id(bb))

aa.append(30)
print(bb)    # 列表为可变类型

print(id(aa))
print(id(bb))


# 引用可做实参

def test1(a):
    print(a)
    print(id(a))

    a += a
    print(a)
    print(id(a))   # 若实参为不可变类型id前后不一致 id发生改变

c = 100
test1(c)

d = [11,22]
test1(d)

'''
可变类型

列表
字典
集合
'''

'''
可变类型

整形
浮点型
字符串
元组
'''