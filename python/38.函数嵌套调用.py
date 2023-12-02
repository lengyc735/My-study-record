# 可以用于简化代码

def testA():
    print('A函数开始——————')
    print('这是A函数')
    print('A函数结束——————')

def testB():
    print('B函数开始——————')
    # 嵌套A函数
    testA()
    print('B函数的结束—————')

testB()

# 案例1 打印横线
# 打印一条横线
def print_line():
    print('-' * 20)

# print_line()

# 打印多条横线
def print_lines(num):
    i = 0
    while i < num:
        print_line()  # 嵌套print_line()
        i += 1

print_lines(3)

# 案例2 简单计算
# 3个数求和
def sum_num(a,b,c):
    return a + b + c

result = sum_num(1,3,5)
print(result)

# 求3个数的平均值
def average_num(a,b,c):
    sumResult = sum_num(a,b,c)
    return sumResult / 3

result2 = average_num(2,3,7)
print(result2)