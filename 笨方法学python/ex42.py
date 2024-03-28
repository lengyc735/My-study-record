stuff = ['Test','This','Out']
print(' '.join(stuff))

class TheThing(object):

    def __init__(self):
        self.number = 0

    def some_function(self):
        print('I got called.')

    def add_me_up(self, more):
        self.number += more
        return self.number
    
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))

print(a.number)
print(b.number)

# class 也就是类就相当于一个函数字典，里面包含了很多函数，这些函数可以被调用，也可以被继承。