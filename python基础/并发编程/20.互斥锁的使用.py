import time
from threading import Thread,Lock

num=0
# 创建一个互斥锁
lock=Lock()
def test1():
    global num
    lock.acquire() #上锁
    for i in range(100000):
        num+=1
    lock.release()  #释放锁
    print('执行test1函数num的值:',num)

def test2():
    global num
    lock.acquire()  # 上锁
    for i in range(100000):
        num+=1
    lock.release()  #释放锁
    print('执行test2函数num的值:',num)

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 多个线程同时修改一个变量，可能造成混乱
# 互斥锁可以 有效避免混乱