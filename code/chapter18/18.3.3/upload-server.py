# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.3.3/upload-server.py

import socket

HOST = '127.0.0.1'
PORT = 8888

f_name = 'test_copy.txt'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('服务器启动...')

    # 创建字节序列对象列表，作为接收数据的缓冲区
    buffer = []
    while True:  # 反复接收数据
        data, _ = s.recvfrom(1024)
        if data:
            flag = data.decode()
            if flag == 'bye':
                break
            buffer.append(data)
        else:
            # 没有接收到数据，进入下次循环继续接收
            continue
    # 将接收的字节序列对象列表合并为一个字节序列对象
    b = bytes().join(buffer)
    with open(f_name, 'w') as f:
        f.write(b.decode())

    print('服务器接收完成。')
