# 1 算数运算符
"""
+ 加 -减 *乘 /除
//取商 %取余 **取幂
优先级（）高于**高于*，/，//，%高于+，-
"""
a = 2 ** 3
b = 9 // 4
c = 9 % 4
d = (1 +2) * 3
print(a,b,c,d)

# 2 赋值运算符(=)

# 单个变量赋值
num = 1
print(num)

# 多个变量赋值
mun1,float1,str1 = 7,1.2,'love'
print(mun1,  float1,  str1)

# 多变量赋相同值
a = b = 7
print(a,   b)

# 3 复合赋值运算符
"""
+= 加法赋值运算符 c += a 等价于 c = c + a
-=   *=   /=   //=    %=  **=
"""
a = 7
a += 1
print(a)

b = 2
b *= 1 + 2  # 会先算等会后面的 b = b * (1 + 2)
print(b)

# 4 比较运算符
"""
== 判断相等 != 不等于  >大于  <小于  >=大于等于  <=小于等于
输出结果均为bool
"""
a = c = 7
b = 3
print(a >= b)
print(a != c)
print(a <= c)

#  5 逻辑运算符
a = 0
b = 1 
c = 2

# and: 与：都真才真，一假则假
print(a > b and b < c)
print((a < b) and (c > b))  # 添加()不会影响结果，可以避免歧义

# or: 或：一真则真，都假才假
print(a > c or b > a)

# not: 取反 
print(not a > c)   # Float 会输出为 Ture

# 5.1 拓展 数字之间的逻辑运算
a = 0 
b = 1 
c = 7
# and运算符，只要有一个值为零结果为零，否则结果为最后一个非零数字
print(a and c)   # 0
print(b and c)   # 7
# or运算符，只有所有值为零才为零，否则结果为第一个非零数字
print(a or b)          # 1
print(a or c or a)     # 7