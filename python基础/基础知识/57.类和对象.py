'''
类
class 类名():
    代码
    ......
'''

'''
对象
对象名 = 类名()

注意：现有类再有对象
'''

# 1.定义类
class washer():
    def wash(self):
        print('洗洗洗衣')
        print(self)

# 2.创建对象
haier = washer()

# 3.验证成果
print(haier)

# 4.对象调用实例方法
haier.wash()

# self 指的是调用该函数的对象本身