
# 颜色框

from tkinter import *
from tkinter.colorchooser import *

root = Tk()
root.geometry('400x150')

def fun():
    s1 = askcolor(color='red',title='选择背景色')
    print(s1)
    # s1的值是:((0.0, 0.0, 255.99609375), '#0000ff')
    root.config(bg=s1[1])

Button(root, text='选择背景色', command=fun).pack()

root.mainloop()