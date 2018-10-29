# coding=utf-8
# 代码文件：chapter18/18.3.2/udp-client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器地址
server_address = ('127.0.0.1', 8888)

# 给服务器端发送数据
s.sendto(b'Hello', server_address)
# 从服务器端接收数据
data, _ = s.recvfrom(1024)
print('从服务器端接收消息：{0}'.format(data.decode()))

# 释放资源
s.close()
