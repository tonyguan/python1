# coding=utf-8
# 代码文件：chapter18/ch18.4.6.py

import urllib.parse

url = 'https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'download.png'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载文件成功')
