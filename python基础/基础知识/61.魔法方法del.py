'''
del()
当删除对象时，python解释器也会默认调用__del__方法
'''

class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __del__(self):
        print(f'{self}对象已经被删除')

haier1 = Washer(10,20)

# <__main__.Washer object at  0x0000028564A5B590>对象已经被删除
del haier1