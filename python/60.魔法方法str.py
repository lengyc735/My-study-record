'''
__str__() 
当使用print输出对象的时候，默认打印对象的内存地址。
如果类定义了__str__方法，那么就会打印从在这个方法中return的数据。
'''

class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        return '这是海尔洗衣机的说明书'
    
haier1 = Washer(10,20)
print(haier1)

