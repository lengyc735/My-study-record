class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼制作配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼')

    
# 创建学校类
class School(object):
    def __init__(self):
        self.kongfu = '[冷氏鸡蛋饼配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作鸡蛋饼')

class Prentice(School,Master):
    # 一个类继承多个父类，如果多个父类有同名的属性和方法，默认使用第一个父类的属性和方法
    # 初始化的原因是：如果不加这个自己的初始化。kongfu的属性值是上一次调用init内的kongfu属性值
    def __init__(self):
        self.kongfu = '[独创鸡蛋饼配方]'    
        self.__money = 70000    # 私有属性，只能在类内部使用，不能继承给子类

    def get_money(self):
        '''获取私有属性'''
        return self.__money
    
    def set_money(self):
        self.__money = 17771

    def __info_print(self):    # 私有方法，只能在类内部使用，不能继承给子类
        '''私有方法，不能继承给子类'''
        print(self.kongfu)
        print(self.__money)

    # 子类调用父类的同名属性和方法:把父类的同名方法和属性再次封装
    def make_Master_cake(self):
        # 父类类名.函数()
        # 初始化的原因：为了调用父类的属性和方法
        Master.__init__(self)
        super(Prentice,self).make_cake()   # 等价于Master.make_cake(self)

        # super().函数()  作用：调用父类方法
        # 有参数写法 super(当前类名，self).函数()
        # 无参数写法 super().函数()
        # super会自动查找父类，调用顺序遵循__mro__类继承顺序

class Grandson(Prentice):
    pass


daqiu = Prentice()
print(daqiu.kongfu)
daqiu.make_cake()

daqiu.make_Master_cake()

print()

xiaoqiu = Grandson()
print(xiaoqiu.kongfu)
xiaoqiu.make_cake()
print(xiaoqiu.get_money())

xiaoqiu.make_Master_cake()

# 结论：如果子类和父类拥有同名属性和方法，子类创建对象调用属性和方法时，调用的是子类的属性和方法