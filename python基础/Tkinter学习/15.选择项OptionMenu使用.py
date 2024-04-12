
# optionmenu使用


from tkinter import *

root = Tk()
root.geometry('200x100')
v = StringVar(root)
v.set('777')
om = OptionMenu(root,v,'777','888','999')

om['width'] = 10
om.pack()

def test1():
    print('最喜欢的数字：',v.get())

Button(root,text='确定',command=test1).pack()

root.mainloop()