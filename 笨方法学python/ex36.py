'''
if 语句的规则
1. if 语句中的条件可以是数字，字符串，列表，元组等，及任何返回结果为布尔值的表达式
2. 任何非零和非空（null）值均为true
3. 0 或者 null为false
4. and 与 or 都是短路逻辑
5. python中没有switch – case语句
6. if 嵌套语句
7. if-elif-else语句
8. 三元运算符
9. assert断言
10. python中没有do-while循环
11. python中没有goto语句
12. break和continue结束本次循环
'''

# 小游戏，要求找到宝剑，打败老虎，解救公主

from sys import exit

baojian = 0
yaoshi = 0

def gongzhu_fangjian():
    print('恭喜你打败了老虎救出了公主')
    print('公主说：我爱你，你要娶我吗？')
    print('A.娶 B.不娶')

    action = input('A or B>  ')

    if action == 'A':
        print('公主上前吻了你')
        exit(0)
    elif action == 'B':
        print('公主眼角流下了泪水')
        exit(0)
    else:
        print('请输入A或者B')
        gongzhu_fangjian()

def laohu_fangjian():
    global baojian, yaoshi
    print("你来到了老虎的房间")
    print('老虎转身看向了你')
    print('你可以选择逃走，或者战斗')
    
    action = input('A.逃跑 B.死战>  ')
    if action == 'A':
        print('你成功逃跑了，你看了看身后，老虎似乎没有追上来')
        print()
        fangjian2()
    elif action == 'B' and baojian == 1:
        if yaoshi == 1:
            print('你选择了死战，你拿出了宝剑，你和老虎展开了激烈的战斗')
            print('你成功击败了老虎，你继续前进') 
            print()  
            gongzhu_fangjian()
        else:
            print('你战胜了老虎，但是你没有钥匙，你无法救出公主')
            print('请找到公主房间的钥匙，再来救出公主')
            print()
            fangjian2()
    elif action == 'B' and baojian == 0:
        print('你没有宝剑，你无法战胜老虎')
        print('你被老虎吃掉了')
        exit(0)
    else:
        print('你只能选择逃跑或者死战')
        laohu_fangjian()

def fangjian2():
    global baojian
    print('你来到了2号房间')
    print('你看到房间左边和前面都有一个门')
    print('你可以选择左边的门，或者前面的门')

    action = input('A.左边 B.前面 C.往回走>  ')

    if action == 'A':
        print('你发现了宝剑，你拿起了宝剑，被传送回了二号房间')
        print()
        baojian = 1
        fangjian2()
    elif action == 'B':
        print('你来到了老虎的房间')
        print()
        laohu_fangjian()
    elif action == 'C':
        print('你回到了一号房间')
        fangjian1()
    else:
        print('你只能选择A，B，C')
        fangjian2()

def fangjian1():
    global yaoshi
    print('想要救出公主需要宝剑和公主房间的钥匙')
    print('你的面前有两个门，你可以选择左边的门，或者右边的门')

    action = input('A.左边 B.右边>  ')
    
    if action == 'B':
        print('找到了钥匙，你拿起了钥匙，被传送回了一号房间')
        print()
        yaoshi = 1
        fangjian1()
    elif action == 'A':
        print('你打开了右边的门')
        print()
        fangjian2()
    else:
        print('你只能选择A或者B')
        fangjian1()

fangjian1() 