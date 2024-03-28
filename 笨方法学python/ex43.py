'''
思路：
三个房间
猜数字
满足条件可进入下一个房间
'''

from random import randint
from sys import exit

class Mygame():

    def __init__(self):
        print('欢迎来到猜数字游戏')
        self.num1 = randint(1,10)
        self.num2 = randint(10,100)
        self.num3 = randint(100,1000) 
    
    def room1(self):
        print('欢迎来到第一个房间')
        print('猜一个1-10的数字')
        times = 0
        while times < 3:
            guess = int(input('\n请输入一个个位数： '))
            if guess == self.num1:
                print('\n恭喜你猜对了')
                print('你将进入下一关')
                self.room2()
            elif guess > self.num1:\
                print('\n猜大了')
            elif guess < self.num1:
                print('\n猜小了')
            else:
                print('\n输入有误，请重新输入')
                self.room1()
            times += 1
        if times == 3:
            print('\n看来你的运气不太好')
            print('游戏结束了,答案是%r' % self.num1)
            exit(0)

    def room2(self):      
        print('欢迎来到第二个房间')
        print('猜一个10-100的数字')
        times = 0
        while times < 5:
            guess = int(input('\n请输入一个2位数： '))
            if guess == self.num1:
                print('\n恭喜你猜对了')
                print('你将进入下一关')
                self.room3()
            elif guess > self.num2:\
                print('\n猜大了')
            elif guess < self.num2:
                print('\n猜小了')
            else:
                print('\n输入有误，请重新输入')
                self.room1()
            times += 1
        if times == 5:
            print('\n看来你的运气不太好')
            print('游戏结束了,答案是%r' % self.num2)
            exit(0)

    def room3(self):
        print('欢迎来到第三个房间')
        print('猜一个100-1000的数字')
        times = 0
        while times < 7:
            guess = int(input('\n请输入一个3位数： '))
            if guess == self.num1:
                print('\n恭喜你猜对了')
                print('游戏结束，你赢了')
                exit(1)
            elif guess > self.num3:\
                print('\n猜大了')
            elif guess < self.num3:
                print('\n猜小了')
            else:
                print('\n输入有误，请重新输入')
                self.room1()
            times += 1
        if times == 7:
            print('\n看来你的运气不太好')
            print('游戏结束了,答案是%r' % self.num3)
            exit(0)

Mygame().room1()