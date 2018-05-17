# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.2.4/tcp-client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('127.0.0.1', 8888))

# 给服务器端发送数据
s.send(b'Hello')
# 从服务器端接收数据
data = s.recv(1024)
print('从服务器端接收消息：{0}'.format(data.decode()))

# 释放资源
s.close()
