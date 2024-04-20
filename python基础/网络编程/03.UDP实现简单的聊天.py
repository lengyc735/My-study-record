from socket import *

udp_socket=socket(AF_INET,SOCK_DGRAM)
# 绑定本地信息
udp_socket.bind(("",7788))
while True:
    recv_data=udp_socket.recvfrom(1024)
    msg=recv_data[0].decode("gb2312")
    print('接收到{}的消息:{}'.format(recv_data[1],msg))
    if msg=='bye':
        break

# 关闭套接字                                
udp_socket.close() 