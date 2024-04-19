import _thread
from time import sleep

def fun1():
    print('开始运行fun1')
    sleep(4)
    print('运行fun1结束')

def fun2():
    print('开始运行fun2')
    sleep(2)
    print('运行fun2结束')

if __name__=='__main__':
    print('开始运行')
    # 创建线程
    _thread.start_new_thread(fun1,())
    _thread.start_new_thread(fun2,())
    sleep(7)  #让主线程休眠是为了让线程能运行完