# 导入模块
from socket import *
from threading import Thread

# 创建UDP套接字对象
udp_socket=socket(AF_INET,SOCK_DGRAM)
# 绑定本地信息
udp_socket.bind(('',7878))
# 接收
def recv_msg():
    while True:
        recv_data=udp_socket.recvfrom(1024)
        print('>>%s:%s'%(recv_data[1],recv_data[0].decode('gb2312')))

# 发送
def send_msg():
    while True:
        addr=('127.0.0.1',8080)
        data=input('<<:')
        udp_socket.sendto(data.encode('gb2312'),addr)

if __name__=='__main__':
    # 创建两个线程
    t1=Thread(target=send_msg)
    t2=Thread(target=recv_msg)
    t1.start()
    t2.start()
    t1.join()
    t2.join()