# 在python中,__xx__()的函数叫做魔法方法，指的是具有特殊功能的函数

# __init__()方法， 作用：初始化对象

class Washer():
    # 定义__init__(),添加实例
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 800

    def print_info(self):
        print('f洗衣机的宽度为{self.width},高度为{self.weight}')

haier1 = Washer()
haier1.print_info()

'''
__init__()方法，在创建一个对象时默认被调用，不需要手动调用
__init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递过去
'''

# 带参数的__init__()方法
class Washer2():
    def __init__(self,width,height):
        self.width = width
        self.height =  height

    def print_info(self):
        print(f'2洗衣机的宽度为{self.width},高度为{self.height}')

haier2 = Washer2(10,20)
haier2.print_info()