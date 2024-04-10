
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
        self.label01 = Label(self,text='这是一个标签',width=10,height=2,bg='black',fg='white')
        self.label01.pack()

        self.label02 = Label(self,text='这是第二个标签',width=15,height=2,bg='green',fg='white',font=('宋体',25))
        self.label02.pack()

        # 图片显示
        global photo   # 把photo声明为全局变量，是为了防止本方法调用完，图片被回收(不显示)
        photo = PhotoImage(file='./3.image.gif')   # 注意：格式只支持 ( gif )
        self.label03 = Label(self,image=photo)
        self.label03.pack()
        
        # 多行文本
        self.label04 = Label(self,text='我爱python\n我是一条狗\n汪汪汪汪',
                             borderwidth=1, relief='solid', justify='right')
        # borderwidth是边框宽度，relief是边框样式，justify是文本对齐方式
        self.label04.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x300+600+300')
    root.title('Label的使用')
    app = Application(master=root)

    root.mainloop()