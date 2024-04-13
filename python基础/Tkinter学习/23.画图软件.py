
'''绘图软件'''

from tkinter import *
from tkinter.colorchooser import *

# 窗口高度 宽度
win_width = 900
win_height = 500

class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None
        self.bgcolor = '#000000'
        self.x = 0
        self.y = 0
        self.fgcolor = '#ff0000'
        self.lastDraw = 0
        self.startDrawFlag = False
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建绘图区域
        self.drawpad = Canvas(root,width=win_width,height=win_height*0.9,bg=self.bgcolor)
        self.drawpad.pack()

        # 创建按钮
        btn_start = Button(root,text='开始',name='start')
        btn_start.pack(side='left',padx='6')
        btn_pen = Button(root,text='画笔',name='pen')
        btn_pen.pack(side='left',padx='6')
        btn_rect = Button(root,text='矩形',name='rect')
        btn_rect.pack(side='left',padx='5')
        btn_clear = Button(root,text='清屏',name='clear')
        btn_clear.pack(side='left',padx='5')
        btn_erasor = Button(root,text='橡皮擦',name='erasor')
        btn_erasor.pack(side='left',padx='5')
        btn_line = Button(root,text='直线',name='line')
        btn_line.pack(side='left',padx='5')
        btn_lineArrow = Button(root,text='箭头直线',name='lineArrow')
        btn_lineArrow.pack(side='left',padx='6')
        btn_color = Button(root,text='颜色',name='color')
        btn_color.pack(side='left',padx='6')

        #  绑定事件
        btn_pen.bind_class('Button','<1>',self.eventManager)
        self.drawpad.bind('<ButtonRelease-1>',self.stopDraw)

        #  增加快捷键
        root.bind('<KeyPress-r>',self.hotkey)
        root.bind('<KeyPress-y>',self.hotkey)
        root.bind('<KeyPress-g>',self.hotkey)
        
    def eventManager(self,event):
        name = event.widget.winfo_name()
        print(name)
        if name=='line':
            self.drawpad.bind('<B1-Motion>',self.myline)
        elif name=='lineArrow':
            self.drawpad.bind('<B1-Motion>',self.mylineArrow)
        elif name=='rect':
            self.drawpad.bind('<B1-Motion>',self.myRect)
        elif name=='pen':
            self.drawpad.bind('<B1-Motion>',self.myPen)
        elif name=='erasor':
            self.drawpad.bind('<B1-Motion>',self.myErasor)
        elif name=='clear':
            self.drawpad.delete('all')
        elif name=='color':
            new_color = askcolor(color=self.fgcolor,title='选择画笔颜色')
            # 注意此处返回值为列表 类似：[(255,0,0),'#ff0000']
            self.fgcolor = new_color[1]

    def stopDraw(self,event):
        '''停止绘画'''
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self,event):
        '''开始绘画'''
        self.drawpad.delete(self.lastDraw)
        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def myline(self,event):
        '''直线'''
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)

    def mylineArrow(self,event):
        '''箭头直线'''
        self.startDraw(event)

        self.lastDraw = self.drawpad.create_line(self.x,self.y,event.x,event.y,arrow=LAST,fill=self.fgcolor)

    def myRect(self,event):
        '''矩形'''
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x,self.y,event.x,event.y,outline=self.fgcolor)

    def myPen(self,event):
        '''画笔'''
        self.startDraw(event)
        self.drawpad.create_line(self.x,self.y,event.x,event.y,fill=self.fgcolor)
        self.x = event.x;  self.y = event.y

    def myErasor(self,event):
        '''橡皮'''
        self.startDraw(event)
        self.drawpad.create_rectangle(event.x-4,event.y-4,event.x+4,event.y+4,fill=self.bgcolor)
        self.x = event.x;  self.y = event.y

    def hotkey(self,event):
        if event.char == 'r':
            self.fgcolor = "#ff0000"
        elif event.char == 'y':
            self.fgcolor = '#ffff00'
        elif event.char == 'g':
            self.fgcolor = '#00ff00'

if __name__ == '__main__':
    root = Tk()
    root.geometry(str(win_width)+'x'+str(win_height))
    root.title('狗叫画图')
    app = Application(master=root)

    root.mainloop()