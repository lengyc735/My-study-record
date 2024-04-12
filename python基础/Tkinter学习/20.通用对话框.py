
'''通用消息框'''

from tkinter import *
from tkinter.messagebox import *

root = Tk(); root.geometry('400x100')

a1 = showinfo(title='不想想标题',message='打个软软糯糯绝绝子的交')
print(a1)

root.mainloop()