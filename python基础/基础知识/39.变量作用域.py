'''
变量作用域指的是变量生效的范围，主要分为两类：局部变量和全局变量
局部变量是定义在函数内部的变量，只在函数内部生效
全局变量指的是在函数内外都可以使用的变量
'''

# 局部变量举例

def test_1(n):
    a = 0
    print(a+n)

test_1(9)
# print(a)  报错：name 'a' is not defind

# 全局变量举例

b = 777

def test_2():
    print(b)

def test_3():
    print(2+b)

def test_4():
    b = 177   # 此处的b是局部变量，与上一个b并不相等
    print(b)

print(b)

def test_5():
    global b  # 声明b是全局变量
    b = 211
    print(b)

print(b)

test_2()
test_3()
test_4()
test_5()