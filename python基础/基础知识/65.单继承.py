# 1.师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '【古法煎饼果子配方】'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2.徒弟类    
class Prentice(Master):
    pass

# 3.创建对象daqiu
daqiu = Prentice()

# 4.对象访问实例属性
print(daqiu.kongfu)