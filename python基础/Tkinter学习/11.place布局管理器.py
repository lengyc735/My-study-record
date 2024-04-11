
# palce布局管理器可以通过坐标精确控制组件位置，适用于灵活的场景

'''
x,y
组件左上角的绝对坐标(相对于窗口)
取值范围：非负整数
'''

'''
relx, rely
组件左上角的坐标(相对于父容器)
0最上边  0.5正中间  1最下边
'''

'''
width, height
组件的宽度和高度
非负整数
'''

'''
relwidth, relheight
组件的宽度和高度(相对于父容器)
与relx,rely取值类似，但是相对于父组件的尺寸
'''

'''
anchor
对齐方式， 左对齐'w', 右对齐'e',顶对其'n',底对其's'
n, s, w, e, nw, sw, se, ne, center(默认)
'''

from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('palce布局管理器')
root['bg']='white'

f1 = Frame(root,width=300,height=200,bg='green')
f1.place(x=30,y=30)

Button(root,text='python').place(relx=0.5,x=80,y=50,relwidth=0.2,relheight=0.5)
Button(f1,text='我是条狗').place(relx=0.5,rely=0.6)
Button(f1,text='我爱狗叫').place(relx=0.4,rely=0.2)

root.mainloop()