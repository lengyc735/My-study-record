'''
面对对象的三大特性：封装、继承、多态

封装：
  1.将属性和方法封装到一个抽象的类中，类是一个抽象的概念，对象是一个具体的实例
  2.封装可以隐藏对象的属性和实现细节，仅对外提供公共访问方式

继承：
  1.子类默认继承父类的所有属性和方法
  2.子类可以重写父类的属性和方法

多态：
  传入不同的对象，产生不同的结果
'''

# 多态是基于继承的

class Dog():
    def work(self):
        print('指哪打哪...')

class Armydog(Dog):      # 继承Dog类
    def work(self):      # 子类重写父类同名方法
        print('追击敌人...')

class Drugdog(Dog):
    def work(self):
        print('追击毒品···')

class Person():
    def work_with_dog(self,dog):    # 传入不同的对象，产生不同的结果
        dog.work()


ad = Armydog()
dd = Drugdog()

bigming = Person()
bigming.work_with_dog(ad)
bigming.work_with_dog(dd)