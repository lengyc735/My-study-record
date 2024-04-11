
# pack布局管理器,按照垂直或者水平排布，默认在父组件中自顶向下垂直添加组件
# 多使用于简单的场景

# pack实现钢琴软件布局

from tkinter import *

root = Tk()
root.geometry('800x300')

# Frame是一个矩形区域，就是用来放置其他子组件
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()

btnText = ('流行风','中国风','日本风','重金属风','轻音乐')

for txt in btnText:
    Button(f1, text=txt).pack(side='left',padx='10')

for i in range(1,20):
    Label(f2,width=5,height=10,borderwidth=1,relief='solid',
          bg='black' if i%2==0 else 'white').pack(side='left',padx=2)
    
root.mainloop()