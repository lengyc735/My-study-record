
# Entry用于输入单行文本

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
        self.label01 = Label(self, text='用户名')
        self.label01.pack()

        # StringVar变量绑定到指定的组件
        # StringVar变量的值发生变化，组件内容也发生变化
        # 组件内容发生变化，StringVar变量的值也发生变化
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1) 
        self.entry01.pack()
        v1.set('admin')   # 设置默认值

        # 创建密码
        self.label02 = Label(self, text='密码')
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show='*') 
        self.entry02.pack()

        self.btn01 = Button(self,text='登录',command=self.login).pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()

        print('去数据库进行比对')
        print('用户名：'+username)
        print('密码：'+pwd)

        if username == '数据库对应的名字' and pwd == '数据库对应的密码':
            messagebox.showinfo('提示','您已成功登录')
        else:
            messagebox.showinfo('提示','登录失败，用户名或密码错误')


if __name__ == '__main__':
    root = Tk()
    root.geometry('300x150+600+300')
    root.title('Entry测试')
    app = Application(master=root)

    root.mainloop()