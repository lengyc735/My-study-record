# 高阶函数是可以把函数作为参数传入

# abs()用于求绝对值
abs(-10)  # 10

# round()用于四舍五入
round(2.7)  # 3
round(2.4)  # 2

def add_num(a,b):
    return abs(a)+abs(b)

result = add_num(-1,2)
print(result)

# 用f来接收函数
def sum_num(a,b,f):
    return f(a)+f(b)

result1 = sum_num(-2,3,abs)
print(result1)

result2 = sum_num(-1.2,1.7,round)
print(result2)