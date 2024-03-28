i = 0
numbers = []

while i < 6:
    print('At the top i is %d' % i)
    numbers.append(i)

    i += 1
    print('Numbers now: ', numbers)
    print('At the bottom i is %d' % i)

print('The numbers: ')

for num in numbers:
    print(num)


# 用函数实现
def  while_me(num):
    i = 0
    numbers = []
    while i < num:
        print('At the top i is %d' % i)
        numbers.append(i)

        i += 1
        print('Numbers now: ', numbers)
        print('At the bottom i is %d' % i)

    print('The numbers: ')

    for num in numbers:
        print(num)

while_me(2)
'''
虽然看似写法差不多，但是函数可以反复调用，
而且可以传入参数，而且函数内部的变量不会影响到函数外部的变量，
也就是说函数可以缩减代码量，提高代码的复用性
'''