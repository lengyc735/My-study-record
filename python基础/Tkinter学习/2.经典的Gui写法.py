
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    '''一个经典的Gui程序的类的写法'''

    def __init__(self, master=None):
        super().__init__(master=None)   # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.btn01 = Button(self)
        self.btn01['text'] = '点我就告诉你个秘密'
        self.btn01.pack()
        self.btn01['command'] = self.show

        # 创建退出按钮
        self.btnQuit = Button(self, text='退出', command=root.destroy)   # root.destroy与master.quit有区别
        self.btnQuit.pack()

    def show(self):
        messagebox.showinfo('秘密','爱老虎油')

if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+600+300')
    root.title('一个经典的GUi程序类的测试')
    app = Application(master=root)

    root.mainloop()