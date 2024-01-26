# 父类
class A(object):
    def __init__(self):
        self.num = 1

    def info_print(self):
        print(self.num)


# 子类
class B(A):
    pass


result = B()
result.info_print()    # 1

# 在python中，所有类默认继承object类，object类是python中的顶级类，所有类都是object类的子类，为派生类