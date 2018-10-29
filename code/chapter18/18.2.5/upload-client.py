# coding=utf-8
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
