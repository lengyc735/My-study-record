
'''记事本'''

from tkinter import *
from tkinter.filedialog import *
from tkinter.colorchooser import *


class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建主菜单栏
        menubar = Menu(root)

        # 创建子菜单
        menuFile = Menu(menubar)
        menuFdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入主菜单
        menubar.add_cascade(label='文件(F)',menu=menuFile)
        menubar.add_cascade(label='编辑(E)',menu=menuFdit)
        menubar.add_cascade(label='帮助',menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label='新建',accelerator='ctrl+n',command=self.newfile)
        menuFile.add_command(label='打开',accelerator='ctrl+o',command=self.openfile)
        menuFile.add_command(label='保存',accelerator='ctrl+s',command=self.savefile)
        menuFile.add_separator()   # 添加分割线
        menuFile.add_command(label='退出',accelerator='ctrl+q',command=self.exit) 

        # 将主菜单栏加到根窗口
        root['menu'] = menubar

        # 增加快捷键
        root.bind('<Control-n>',lambda event:self.newfile())
        root.bind('<Control-o>',lambda event:self.openfile())
        root.bind('<Control-s>',lambda event:self.savefile())
        root.bind('<Control-q>',lambda event:self.exit())

        # 文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()

        # 创建快捷菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label='背景颜色',command=self.openAskcolor)

        # 为右键绑定事件
        root.bind('<Button-3>',self.createContextMenu)

    def newfile(self):
        self.textpad.delete('1.0','end')   # 把text控件中所有内容清空，避免内容重复
        self.filename = asksaveasfilename(title='另存为',initialfile='未命名.txt',
                                          filetypes=[('文本文档','*.txt')],
                                          defaultextension='.txt')  # defaultextension为默认后缀
        self.savefile()

    def openfile(self):
        self.textpad.delete('1.0','end')   # 把text控件中所有内容清空，避免内容重复
        with askopenfile(title='打开文本文件')as f:
            self.textpad.insert(INSERT,f.read())
            self.filename = f.name

    def savefile(self):
        with open(self.filename,'w')as f:
            c = self.textpad.get(1.0,END)
            f.write(c)

    def exit(self):
        root.quit()

    def openAskcolor(self):
        '''快捷菜单 背景颜色'''
        s1 = askcolor(color='red',title="选择背景颜色")
        self.textpad.config(bg=s1[1])

    def createContextMenu(self,event):
        # 菜单在鼠标右键单击位置弹出
        self.contextMenu.post(event.x_root,event.y_root)

if __name__ == '__main__':
    root = Tk()
    root.geometry('600x300')
    root.title('狗叫记事本')
    app = Application(master=root)

    root.mainloop()