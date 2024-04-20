from socket import *

# 创建服务器端套接字对象
client_socket=socket(AF_INET,SOCK_STREAM)
# 调用connect方法与服务器建立连接
client_socket.connect(('127.0.0.1',7788))
while True:
    # 客户端接收消息
    recv_data=client_socket.recv(1024)
    print('接收消息:',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8')=='bye':
        break
    # 客户端发送消息
    msg=input('请输入要发送的消息:')
    client_socket.send(msg.encode('utf-8'))
client_socket.close()