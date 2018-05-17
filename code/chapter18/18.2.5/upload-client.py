# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 配套视频课程：http://www.zhijieketang.com/classroom/10/courses

# 代码文件：chapter18/18.2.5/upload-client.py

import socket

HOST = '127.0.0.1'
PORT = 8888
f_name = 'coco2dxcplus.jpg'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    with open(f_name, 'rb') as f:
        b = f.read()
        s.sendall(b)
        print('客户端上传数据完成。')
