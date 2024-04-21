from socket import *
from threading import Thread

flag=True
def readMsg(client_socket):
    while flag:
        recv_data=client_socket.recv(1024)
        print('收到',recv_data.decode('utf-8'))

def writeMsg(client_socket):
    global flag
    while flag:
        msg=input('>>')
        msg=user_name+'说:'+msg
        client_socket.send(msg.encode('utf-8'))
        # 如果输入bye就下线
        if msg.endswith('bye'):
            flag=False
            break

# 创建客户端套接字对象
client_socket=socket(AF_INET,SOCK_STREAM)
# 调用connect连接服务器
client_socket.connect('127.0.0.1',7788)
user_name=input('请输入用户名:')
# 开启一个线程处理客户端 读取消息
t1=Thread(target=readMsg,args=(client_socket,))
t1.start()
# 开启一个线程吹客户端的发送消息
t2=Thread(target=writeMsg,args=(client_socket,))
t2.start()
t1.join()
t2.join()
client_socket.close()