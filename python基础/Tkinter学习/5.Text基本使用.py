
# Text用于输入多行文本

from tkinter import *
import webbrowser


class Application(Frame):
    '''一个经典的Gui程序的类的写法'''

    def __init__(self, master=None):
        super().__init__(master=None)   # super代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        '''创建组件'''
        self.w1 = Text(root, width=40, height=12, bg='gray')
        # 宽度20个字母(10个汉字)，高度一个行高
        self.w1.pack()

        self.w1.insert(1.0, '0123456789\nabcdefg')
        self.w1.insert(2.3, '桃李春风一杯酒\n江湖夜雨十年灯')

        Button(self,text='重复插入文本',command=self.insertText).pack(side='left')
        Button(self,text='返回文本',command=self.returnText).pack(side='left')
        Button(self,text='添加图片',command=self.addImage).pack(side='left')
        Button(self,text='添加组件',command=self.addWidget).pack(side='left')
        Button(self,text='通过tag精确控制文本',command=self.textTag).pack(side='left')


    def insertText(self):
        # INSERT索引表示在光标处插入
        self.w1.insert(INSERT, '【插入】')
        # END索引号表示在最后插入
        self.w1.insert(END, '[sxt]')

    def returnText(self):
        # Indexes(索引)是用来指向Text组件中文本的位置，Text的组件索引也是对应实际字符之间的位置
        # 核心：行号 以1开始，列号以0开始
        print(self.w1.get(1.2, 1.6))
        # self.w1.insert(1.8, 'python')
        print('所有文本内容：\n'+self.w1.get(1.0, END))

    def addImage(self):
        # global
        # self.photo = photoImage(file='没有')
        # self.w1.image_create(END， image=sef.photo)
        print('emm--没有图片')
        

    def addWidget(self):
        b1 = Button(self.w1, text='我是一条狗')
        # 在text创建组件的命令
        self.w1.window_create(INSERT, window=b1)

    def textTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, 'good good study,day day up\n我是一条狗\n我是一头猪\nbing搜索')
        self.w1.tag_add('good',1.0, 1.9)
        self.w1.tag_config('good', background='yellow',foreground='red')

        self.w1.tag_add('bing',4.0, 4.2)
        self.w1.tag_config('bing', underline=True)
        self.w1.tag_bind('bing', '<Button-1>', self.webshow)

    def webshow(self,event):
        webbrowser.open('https://www.bing.com')

if __name__ == '__main__':
    root = Tk()
    root.geometry('850x500+600+300')
    root.title('text测试')
    app = Application(master=root)

    root.mainloop()