
# grid布局实现计算机ui，注:无功能，仅ui

from tkinter import *


class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        btnText = (('MC','M+','M-','MR'),
                   ('c','+-','/','*'),
                   (7,8,9,'-'),
                   (4,5,6,'+'),
                   (1,2,3,'='),
                   (0,'.'))
        
        Entry(self).grid(row=0,column=0,columnspan=4,pady=10)

        for rindex,r in enumerate(btnText):
            for cindex,c in enumerate(r):
                if c == '=':
                    Button(self,text=c,width=2)\
                    .grid(row=rindex+1,column=cindex,rowspan=2,sticky=NSEW)
                elif c == 0:
                    Button(self,text=c,width=2)\
                    .grid(row=rindex+1,column=cindex,columnspan=2,sticky=NSEW)
                elif c == '.':
                    Button(self,text=c,width=2)\
                    .grid(row=rindex+1,column=cindex+1,sticky=NSEW)
                else:
                    Button(self,text=c,width=2)\
                    .grid(row=rindex+1,column=cindex,sticky=NSEW)

if __name__ == '__main__':
    root = Tk()
    root.geometry('300x400+200+300')
    root.title('grid计算机布局')
    app = Application(master=root)

    root.mainloop()