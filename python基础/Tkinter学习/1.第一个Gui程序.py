
from tkinter import *
from tkinter import messagebox


# 创建一个窗口对象
root = Tk()  

# 设置窗口标题
root.title('第一个GUI程序')
root.geometry('500x300+600+300')

# 创建一个Button对象
btn_01 = Button(root)
btn_01["text"] = '点我，毁灭世界'

# 将按钮放到窗口上
btn_01.pack()  

def test_1(e):
    messagebox.showinfo('警告','大胆，竟敢想毁灭世界')

btn_01.bind('<Button-1>',test_1)

# 进入消息循环
root.mainloop()   # 其实就是个循环，不断的刷新


'''
常用组件汇总：

Label:标签              用于显示不可编辑的文本或图标
Button:按钮             用于触发事件
Entry:输入框            用于输入单行文本
Text:文本框             用于输入多行文本
Frame:框架              用于将组件分组
Checkbutton:复选框      用于选择多个选项
Radiobutton:单选框      用于选择一个选项
Listbox:列表框          用于显示列表
Scale:滑块              用于选择范围值
Scrollbar:滚动条        用于滚动组件
Canvas:画布             用于绘制图形
Menu:菜单               用于显示菜单
Menubutton:菜单按钮     用于显示菜单按钮
Message:消息框          用于显示消息
PhotoImage:图片         用于显示图片
BitmapImage:图片        用于显示位图
Spinbox:数字框          用于输入数字
PanedWindow:分割窗口    用于分割窗口
Labelframe:标签框       用于显示标签框
Toplevel:顶层窗口       用于显示顶层窗口
'''