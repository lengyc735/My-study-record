from socket import *

# 创建服务器端套接字对象
server_socket=socket(AF_INET,SOCK_STREAM)
# 绑定端口
server_socket.bind(('',7788))
# 设置监听
server_socket.listen()
# 等待客户端连接
client_socket,client_info=server_socket.accept()
# 接收数据
recv_data=client_socket.recv(1024)
print('接收到%s的消息:%s'%(client_info,recv_data.decode('gb2312')))
# 关闭连接
client_socket.close()
server_socket.close()