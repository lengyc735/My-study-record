# 用函数完成1+2的运算
def add_num1():
    result = 1 + 2
    print(result)

add_num1()

# 参数会让函数变得灵活

# 用参数形式传入真实数据，做加法
def add_num2(a,b):
    result = a + b
    print(result)

add_num2(7,5)
# 注意定义函数的a,b为形参；调用函数的7，5为实参
#调用函数实参个数应该与形参个数相等，不然会报错