from socket import *

# 创建客户端套接字对象
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1',7788))
# 客户端发送消息
client_socket.send('hello'.encode('gb2312'))
# 客户接收服务器消息
recv_data = client_socket.recv(1024)
print('接收消息:',recv_data.decode('gb2312'))
# 关闭客户端套接字
client_socket.close()