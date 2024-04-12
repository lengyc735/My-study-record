# 滑块Scale使用

from tkinter import *

root = Tk();root.geometry('400x150')

def test(value):
    print('滑块的值：',value)
    newFont = ('宋体',int(value)//2)
    a.config(font=newFont)

s1 = Scale(root,from_=10,to=50,length=300,tickinterval=5,orient=HORIZONTAL,command=test)
# from_是开始位置,to是结束位置，length滑动条长度(单位：像素)，tickinterval是步长，orient是水平或垂直(默认垂直)
s1.pack()

a = Label(root,text='我巨爱狗叫',width=10,height=1,bg='black',fg='white')
a.pack()

root.mainloop()