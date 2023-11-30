"""
语法：
if 条件1:
    条件1成立执行的代码
    条件1成立执行的代码

    if 条件2:
        条件2成立执行的代码        #注意：缩进为两个制表符 8个空格
        条件2成立执行的代码        #注意:条件2的if也是出于条件1的缩进关系内部
"""

# 案例：判断能否上车，若能上车能否坐下
money = 1
seat = 0
if money >= 1:
    print('土豪请上车')
    if seat >= 1:
        print('有座位，可以坐下')
    else:
        print('没位置，不能坐下')
else:
    print('钱不够，不能上车')
    
#  综合应用 出拳游戏
import random
player = int(input('请出拳：0--石头；1--剪刀;2--布：'))
computer = random.randint(0,2)
print(f'电脑出的是{computer}')
if (player == 0) and (computer == 1) or (player == 1) and (computer == 2) or (player ==2) and (computer == 1):
    print('玩家获胜哈哈哈')
elif player == computer:
    print('平局，别走')
else:
    print('电脑获胜')

# 三目运算符
"""
语法
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
"""
a = 1
b = 2
c = a if a > b else b + a
print(c)