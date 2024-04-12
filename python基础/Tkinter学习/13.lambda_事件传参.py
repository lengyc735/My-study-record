
from tkinter import *

root = Tk()
root.geometry('450x70')

def mouseTest1():
    print('command方式，简单情况:不涉及获取event对象，可以使用')

def mouseTest2(a,b):
    print('a={},b={}'.format(a,b))

Button(root,text='测试command1',command=mouseTest1).pack(side='left')
Button(root,text='测试command2',command=lambda: mouseTest2('狗叫','汪汪汪')).pack(side='left')

root.mainloop()