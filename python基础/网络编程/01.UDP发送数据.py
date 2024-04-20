# 导入模块
from socket import socket,AF_INET,SOCK_DGRAM
# 创建UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)
# 创建接收信息的地址
addr=('127.0.0.1',8080)  # 本地地址,数据类型为元组
# 键盘接收发送到消息
data=input("请输入要发送的消息：")
# 调用sendto方法发送消息
udp_socket.sendto(data.encode('gb2312'),addr)  # 网络助手使用的编码为gb2312
# 关闭套接字
udp_socket.close()