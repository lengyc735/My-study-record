""""
[while循环嵌套语法]
while 条件1:
    条件1成立执行的代码
    .......
    while 条件2:
        条件2成立执行的代码
        .......
"""

i = 1
while i < 4:
    j = 0
    while j < 3:
        print('我爱你')
        j += 1
    print('我恨你')
    print('我要毁灭世界!!!!')
    i += 1

# 打印5行星号，一行5个
j = 0
while j < 5:
    i = 0
    while i <= 4:
        print('*', end='')
        i += 1
    print()    # 借助print默认换行
    j += 1

# 打印三角形*号
j = 0
while j < 5:
    i = 0
    while i <= j:
        print('*',end='')
        i += 1
    print()
    j += 1

# 九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i*j}',end="\t")
        i += 1
    print()
    j += 1