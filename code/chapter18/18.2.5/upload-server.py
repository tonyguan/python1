# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.2.5/upload-server.py

import socket

HOST = ''
PORT = 8888

f_name = 'coco2dxcplus_copy.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print('服务器启动...')

    while True:
        with s.accept()[0] as conn:
            # 创建字节序列对象列表，作为接收数据的缓冲区
            buffer = []
            while True:  # 反复接收数据
                data = conn.recv(1024)
                if data:
                    # 接收的数据添加到缓冲区
                    buffer.append(data)
                else:
                    # 没有接收到数据则退出
                    break
            # 将接收的字节序列对象列表合并为一个字节序列对象
            b = bytes().join(buffer)
            with open(f_name, 'wb') as f:
                f.write(b)

            print('服务器接收完成。')
