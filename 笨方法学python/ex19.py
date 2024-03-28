def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d chesses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")



print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combile the two , variables and math:")

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# 例子: 用函数写出两队比分
def bf(a, b):
    if type(a) and type(b) != int: 
        print('参数类型错误')
    else:
        print('a队得分是: % d' % a)
        print('b队得分是: % d' % b)
        if a > b:
            print(f'a队胜出b队{a - b}分')
        elif a < b:
            print(f'b队胜出a队{b - a}分')
        else:
            print(f'a队:b队比分是{a}:{b},平局,即将进入加时赛')

bf(3 * 5 + 9 * 2 + 1 * 7, 3 * 7 + 2 * 4 + 1 * 9)

c = 3 * 5 + 9 * 2 + 1 * 7
b = 3 * 7 + 2 * 4 + 1 * 9
bf(c,b)
bf(b + 3, c + 7)

import random
bf(random.randint(0,100),random.randint(0,100))