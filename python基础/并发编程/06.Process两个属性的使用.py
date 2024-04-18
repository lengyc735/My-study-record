import multiprocessing
import time
# 定义执行任务的函数
def clock(interval):
    for i in range(3):
        print('当前时间：{}'.format(time.time()))
        time.sleep(interval)

if __name__=='__main__':
    #  创建子进程
    p=multiprocessing.Process(target=clock,args=(1,))
    p.start()
    p.join()
    print('p.id:',p.pid)
    print('p.name:',p.name)
    print('p.is_alive:',p.is_alive())