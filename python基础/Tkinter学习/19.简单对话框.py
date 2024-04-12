
# 简单对话框

from tkinter import *
from tkinter.simpledialog import *

root = Tk(); root.geometry('400x100')

def fun():
    a = askinteger(title='输入年龄',prompt='请输入年龄',initialvalue=18,minvalue=1,maxvalue=150)
    # askstrking,askfloat框使用方式一样
    show['text'] = a

Button(root,text='敢问芳龄？请输入：',command=fun).pack()

show = Label(root,width=40,height=3,bg='green')
show.pack()

root.mainloop()