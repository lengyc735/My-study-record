
# grid表格布局，采用表格结构组织组件,可以跨行和跨列操作

''' 
选项                   说明                                取值范围
column           单元格的列号                          从0开始的正整数
conumnspan       跨列，跨越的行数                          正整数
row               行(与列类似)
rowspan
ipadx, ipady    设置子组件之间的间隔，x方向或y方向      非浮点数，默认0.0
padx, pady      设置与之并列的组件之间的间隔
sticky          组件紧贴所在单元格的某一角，             n, s, w, e, nw
                对应东南西北中以及4个角                 sw, se, ne, center(默认)
'''


from tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0,column=0)
        self.entry01 = Entry(self)
        self.entry01.grid(row=0,column=1)
        Label(self, text='用户名为手机号').grid(row=0,column=2)

        Label(self, text='密码').grid(row=1, column=0)
        Entry(self, show='*').grid(row=1,column=1)

        Button(self, text='登录').grid(row=2, column=1, sticky=EW)
        Button(self, text='取消').grid(row=2, column=2, sticky=E)

if __name__ == '__main__':
    root = Tk()
    root.geometry('600x300+200+300')
    root.title('grid布局')
    app = Application(master=root)

    mainloop()