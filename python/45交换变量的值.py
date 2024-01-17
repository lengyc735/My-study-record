"""
方法1
1.定义中间临时变量
2.把a的数据储存到c 做保存
3.把b的数据储存到a
4.把c的数据赋值到a
"""
a = 10
b = 20
c = 0

c = a
a = b
b = c
print(a)
print(b)

# 方法2
m, n = 1, 2
m, n = n, m
print(m)
print(n)