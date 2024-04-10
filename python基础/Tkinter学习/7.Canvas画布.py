
from tkinter import *
import random

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.canvas = Canvas(self, width=350, height=250, bg='green')
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆 坐标两双为椭圆的左上角和底部右下角
        oval = self.canvas.create_oval(50, 50, 100, 100)

        global Photo
        self.photo = PhotoImage(file='./3.image.gif')
        self.canvas.create_image(150, 170,image=self.photo)

        Button(self, text='画10个矩形', command=self.drawRecrt).pack(side='left')

    def drawRecrt(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas['width'])//2)
            y1 = random.randrange(int(self.canvas['height'])//2)
            x2 = x1 + random.randrange(int(self.canvas['width'])//2)
            y2 = y1 + random.randrange(int(self.canvas['height'])//2)
            self.canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x300+200+300')
    root.title('canvas画布')
    app = Application(master=root)

    mainloop()