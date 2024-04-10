
# 测试Radiobutton组件的基本用法，使用面向对象的方式

from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.v = StringVar();
        self.v.set('F')

        self.r1 = Radiobutton(self, text='男', value='M', variable=self.v)
        self.r2 = Radiobutton(self, text='女', value='F', variable=self.v)

        self.r1.pack(side='left'); self.r2.pack(side='left')

        Button(self, text='确定', command=self.confirm).pack(side='left')

    def confirm(self):
        messagebox.showinfo('测试', '您选择的性别是：' + self.v.get())

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x50+200+300')
    app = Application(master=root)

    mainloop()