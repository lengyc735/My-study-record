from socket import *
from threading import Thread

sockets=[]
def main():
    #创建server_socket套接字对象
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口
    server_socket.bind(('',7788))
    # 监听
    server_socket.listen()
    # 接收客户端的请求
    while True:
        client_socket,client_info=server_socket.accept()
        sockets.append(client_socket)
        # 开启线程处理当前客户端的请求
        t=Thread(target=redMsg,args=(client_socket,))
        t.start()

def redMsg(client_socket):
    # 读取客户端发来的消息
    while True:
        recv_data=client_socket.recv(1024)
        # 如果接收到的消息结尾是bye，则在线客户端列表移除客户端
        if recv_data.decode('utf-8').endswith('bye'):
            sockets.remove(client_socket)
            client_socket.close()
            break
        # 将消息发送给所有在线客户端
        # 遍历所有在线客户端列表
        if len(recv_data)>0:
            for socket in sockets:
                socket.send(recv_data)

if __name__=='__main__':
    main()