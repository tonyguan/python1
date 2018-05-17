# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.2.4/tcp-server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen()
print('服务器启动...')

# 等待客户端连接
conn, address = s.accept()
# 客户端连接成功
print(address)

# 从客户端接收数据
data = conn.recv(1024)
print('从客户端接收消息：{0}'.format(data.decode()))
# 给客户端发送数据
conn.send('你好'.encode())

# 释放资源
conn.close()
s.close()
