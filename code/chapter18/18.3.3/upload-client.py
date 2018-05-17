# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.3.3/upload-client.py

import socket

HOST = '127.0.0.1'
PORT = 8888
f_name = 'test.txt'

# 服务器地址
server_address = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    with open(f_name, 'r') as f:
        while True:  # 反复从文件中读取数据
            data = f.read(1024)
            if data:
                # 发送数据
                s.sendto(data.encode(), server_address)
            else:
				# 发送结束标志
                s.sendto(b'bye', server_address)
                # 文件中没有可读取的数据则退出
                break

        print('客户端上传数据完成。')
