import struct
from socket import *

filename=input('请输入要下载的文件名(需要加上后缀):')
server_ip='127.0.0.1'
# 封装读的请求
send_data=struct.pack('!H%dsb5sb'%len(filename),1,filename.encode(),0,'octet'.encode(),0)
# 数据包的格式是：操作码（1表示读请求）、文件名、0字节、模式（这里是"octet"，表示二进制模式）、0字节
# 创建套接字
udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.sendto(send_data,(server_ip,69)) #读写端口默认是69
# 本地创建一个文件
f=open(filename,'ab')
while True:
    recv_data=udp_socket.recvfrom(1024)
    # print(recv_data)
    # 获取操作码
    cmd_code,ack_num=struct.unpack('!HH',recv_data[0][:4])
    #  判断操作码是否是5如果是5则表示出错
    if cmd_code==5:
        print('文件不存在')
        break
    # 写入文件
    f.write(recv_data[0][4:])
    if len(recv_data[0])<516:
        break
    # 发送确认包
    send_ack=struct.pack('!HH',4,ack_num)
    rand_port=recv_data[1][1] #  获取服务器发送数据的随机端口
    udp_socket.sendto(send_ack,rand_port)