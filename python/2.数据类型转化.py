#str(x)将其数据类型转化为字符串
num1 = 1
num2 = 1.0
print(str(num1),end = '\    ')
print(type(num1),type(str(num1)))
#float(x).....转化为浮点数
print(float(num1),end = "\  ")
print(type(num1),type(float(num1)))
print(str(num2),type(str(num2)))

list1 = [10,20,30]
print(str(list1),end = '          ')
print(tuple(list1))

# eval--计算在字符串中的有效python表达式，并返回一个对象
str1 = '1'
str2 = '(1000,2000,3000)'
str3 = '[1,2,3]'
print(eval(str1),type(eval(str1)))
print(eval(str2),type(eval(str2)))
print(eval(str3),type(eval(str3)))