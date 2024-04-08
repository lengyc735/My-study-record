'''
类属性就是 类对象 所拥有的属性，它被 该类的所有实例对象 所共有
类属性可以使用 类对象 或 实例对象 访问
'''

class Dog():
    tooth = 10


wangcai = Dog()
xiaohei = Dog()

print(Dog.tooth)      # 10
print(wangcai.tooth)  # 10
print(xiaohei.tooth)  # 10

'''
类属性的优点：
    1.记录的某项数据 始终保持一致时，则定义类属性
    2.实例属性 要求 每个对象 为其 单独开辟一份内存空间 来记录数据，
      而 类属性为全类所共有，仅占用一份内存，更加节省内存空间
'''


'''
类属性只能通过类对象修改，不能通过实例对象修改，
如果通过实例对象修改类属性，表示的是创建了一个实例属性
'''
print()
# 通过类对象修改类属性
Dog.tooth = 7
print(Dog.tooth)     # 7
print(wangcai.tooth) # 7
print(xiaohei.tooth) # 7 

print()

# 通过实例对象修改类属性
wangcai.tooth = 11
print(Dog.tooth)      # 7
print(wangcai.tooth)  # 11
print(xiaohei.tooth)  # 7