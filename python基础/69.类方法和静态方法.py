'''
类方法：
  当方法中需要使用类的属性(如访问私有属性)时，可以使用类方法
  类方法的第一个参数必须是类对象，一般以cls作为第一个参数
  类方法一般和类属性配合使用
'''

class Dog():
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

wangcai = Dog()
result = wangcai.get_tooth()
print(result)      # 10


'''
静态方法特点：
  1.需要通过装饰器 @staticmethod 来进行修饰，静态方法既不需要传递类对象也不需要传递实例对象(形参没有self/cls)
    静态方法 也能够通过实例对象和类对象去访问
  2.静态方法 一般是一些工具方法，与类对象和实例对象无关，能通过实例对象和类对象去访问

静态方法使用场景：
  1.当方法中 既不需要使用实例对象(如实例对象，实例属性)，也不需要使用类对象(如类属性、类方法、创建实例等)时，定义静态方法
  2.取消不需要的参数传递，有利于 减少不必要的内存占用和性能消耗
'''

class Cat():
    @staticmethod
    def info_print():     # 注意此处无形参
        print('这是一个猫类，用于创建猫实例...')

# 通过类对象调用静态方法
Cat.info_print()  # 这是一个猫类，用于创建猫实例...

# 通过实例对象调用静态方法
tom = Cat()
tom.info_print()